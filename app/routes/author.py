from flask import Blueprint, render_template, redirect, url_for, request
from app.services import AuthorService
from app.forms import AuthorForm

author_bp = Blueprint("author", __name__)
author_service = AuthorService()

@author_bp.route("/author/add", methods=['POST'])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        author_service.add_author(name=form.name.data, country=form.country.data)
        return redirect(url_for('author.author'))

@author_bp.route("/author", methods=['GET'])
def author():
    form = AuthorForm()
    authors = author_service.get_all()
    total_authors = len(authors)  
    page = request.args.get("page", 1, type=int)  
    per_page = 5
    start = (page-1) * per_page
    end = start + per_page

    paginated_authors = authors[start:end]
    return render_template("author/author.html",
                            form=form,
                            authors = paginated_authors,
                            page=page,
                            per_page=per_page,
                            total_pages=(total_authors // per_page) + (1 if total_authors % per_page else 0),
                           )

@author_bp.route("/author/delete/<int:id>",methods=['GET', 'DELETE'])
def delete_author(id : int):
    if author_service.delete(id):
        return redirect(url_for('author.author'))

@author_bp.route("/author/update",methods=['POST'])
def update_author():
    form = AuthorForm()
    author_id = request.form.get("id")
    if author_id:
        if form.validate_on_submit():
            if author_service.update(id=author_id, name=form.name.data, country=form.country.data):
                return redirect(url_for('author.author'))