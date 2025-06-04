from flask import Blueprint, render_template, redirect, url_for
from app.services import AuthorService
from app.forms import AddAuthorForm

author_bp = Blueprint("author", __name__)
author_service = AuthorService()

@author_bp.route("/author/add", methods=['GET', 'POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        author_service.add_author(name=form.name.data, country=form.country.data)
        return redirect(url_for('author.author'))
    return render_template('author/add_author.html', form=form)

@author_bp.route("/author", methods=['GET'])
def author():
    form = AddAuthorForm()
    authors = author_service.get_all()
    return render_template("author/author.html", form=form, authors = authors)

@author_bp.route("/author/delete/<int:id>",methods=['GET', 'DELETE'])
def delete_author(id : int):
    if author_service.delete(id):
        return redirect(url_for('author.author'))