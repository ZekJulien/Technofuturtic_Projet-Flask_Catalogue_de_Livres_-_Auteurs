from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.services import BookService, AuthorService, CategoryService
from app.forms import BookForm

book_bp = Blueprint("book", __name__)
book_service = BookService()
author_service = AuthorService()
catgories_service = CategoryService()

@book_bp.route("/book", methods=['GET'])
def book():
    form = BookForm()
    authors = author_service.get_all()
    categories = catgories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories]
    #books = []
    return render_template("book/book.html", form=form, authors=authors, categories=categories)


@book_bp.route("/book/add", methods=['POST'])
def add_book():
    form = BookForm()
    authors = author_service.get_all()
    categories = catgories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories]
    if form.validate_on_submit():
        book_service.add_book(title=form.title.data, genre=form.title.data, publication_date=form.publication_date.data, id_author=form.id_author.data, category_ids=form.categories.data)
        return redirect(url_for('book.book'))
    return render_template(
        "book/book.html",
        form=form,
        authors=authors,
        show_add_modal_on_error=True
    )