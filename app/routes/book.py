from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.services import BookService, AuthorService, CategoryService
from app.forms import BookForm

book_bp = Blueprint("book", __name__)
book_service = BookService()
author_service = AuthorService()
catgories_service = CategoryService()

@book_bp.route("/book", methods=['GET'])
def book(form = None, show_add_modal_on_error=False, show_update_modal_on_error=False, update_book_id : int | None = None):
    if form is None:  
        form = BookForm()
    authors = author_service.get_all()
    categories = catgories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories]
    books = book_service.get_all()
    authors_dict = {author.id: author for author in authors}
    return render_template("book/book.html", form=form, authors=authors_dict, books = books, show_add_modal_on_error=show_add_modal_on_error, show_update_modal_on_error=show_update_modal_on_error, update_book_id = update_book_id if show_update_modal_on_error else None)


@book_bp.route("/book/add", methods=['POST'])
def add_book():
    form = BookForm()
    categories = catgories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories] 
    if form.validate_on_submit():
        book_service.add_book(title=form.title.data, genre=form.genre.data, publication_date=form.publication_date.data, id_author=form.id_author.data, category_ids=form.categories.data)
        return redirect(url_for('book.book'))
    return book(form=form, show_add_modal_on_error=True)

@book_bp.route("/book/delete/<int:id>",methods=['GET', 'DELETE'])
def delete_book(id : int):
    if book_service.delete(id):
        return redirect(url_for('book.book'))
    
@book_bp.route("/book/update", methods=['POST'])
def update_book():
    form = BookForm()
    categories = catgories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories]
    book_id = request.form.get("id")
    if form.validate_on_submit():
        if book_service.update(
            id=book_id,
            title=form.title.data,
            genre=form.genre.data,
            publication_date=form.publication_date.data,
            id_author=form.id_author.data,
            category_ids=form.categories.data
        ):
            return redirect(url_for("book.book"))   
    return book(form=form, show_update_modal_on_error=True, update_book_id=book_id)


