from flask import Blueprint, render_template, redirect, url_for, request
from app.services import BookService, AuthorService, CategoryService
from app.forms import BookForm

book_bp = Blueprint("book", __name__)
book_service = BookService()
author_service = AuthorService()
categories_service = CategoryService()


def init_book_form(form: BookForm = None):
    """
    Initializes the book form with categories and authors.
    If no form is provided, a new BookForm instance is created.
    arguments:
    form: BookForm - An instance of BookForm to be initialized.
    returns:
    BookForm - The initialized form with categories and authors.
    """
    form = form or BookForm()
    categories = categories_service.get_all()
    form.categories.choices = [(category.id, category.name) for category in categories]
    return form


def render_book_page(form: BookForm = None, show_add_modal_on_error: bool = False,
                     show_update_modal_on_error: bool = False, update_book_id: int = None):
    """
    Renders the book page with the provided form and options for modals.
    arguments:
    form: BookForm - An instance of BookForm to be rendered.
    show_add_modal_on_error: bool - Flag to show the add modal on error.
    show_update_modal_on_error: bool - Flag to show the update modal on error.
    update_book_id: int - The ID of the book to be updated, if applicable.
    returns:
    Rendered template for the book page.
    """
    form = init_book_form(form)
    authors = author_service.get_all()
    authors_dict = {author.id: author for author in authors}
    all_books = book_service.get_all()  
    total_books = len(all_books)  
    page = request.args.get("page", 1, type=int)  
    per_page = 5
    start = (page-1) * per_page
    end = start + per_page

    paginated_books = all_books[start:end]
    return render_template(
        "book/book.html",
        form=form,
        authors=authors_dict,
        books=paginated_books,
        page=page,
        per_page=per_page,
        total_pages=(total_books // per_page) + (1 if total_books % per_page else 0),
        show_add_modal_on_error=show_add_modal_on_error,
        show_update_modal_on_error=show_update_modal_on_error,
        update_book_id=update_book_id if show_update_modal_on_error else None
    )


@book_bp.route("/book", methods=['GET'])
def book():
    """
    Renders the book page with all books, authors, and categories.
    This function initializes the book form and retrieves all authors and books.
    returns:
    Rendered template for the book page.
    """
    return render_book_page()


@book_bp.route("/book/add", methods=['POST'])
def add_book():
    """
    Handles the addition of a new book.
    This function initializes the book form, validates it, and adds a new book
    if the form is valid. If the form is not valid, it re-renders the book page
    with the form and an error modal.
    returns:
    Redirects to the book page if successful, or re-renders the book page with errors.
    """
    form = BookForm()
    init_book_form(form)
    if form.validate_on_submit():
        book_service.add_book(
            title=form.title.data,
            genre=form.genre.data,
            publication_date=form.publication_date.data,
            id_author=form.id_author.data,
            category_ids=form.categories.data
        )
        return redirect(url_for('book.book'))
    return render_book_page(form, show_add_modal_on_error=True)


@book_bp.route("/book/delete/<int:id>", methods=['GET', 'DELETE'])
def delete_book(id: int):
    """
    Deletes a book by its ID.
    This function calls the book service to delete the book and redirects to the book page.
    arguments:
    id: int - The ID of the book to be deleted.
    returns:
    Redirects to the book page after deletion.
    """
    if book_service.delete(id):
        return redirect(url_for('book.book'))
    return redirect(url_for('book.book'))


@book_bp.route("/book/update", methods=['POST'])
def update_book():
    """
    Handles the update of an existing book.
    This function initializes the book form, retrieves the book ID from the request,
    validates the form, and updates the book if the form is valid. If the form is not valid,
    it re-renders the book page with the form and an error modal.
    returns:
    Redirects to the book page if successful, or re-renders the book page with errors.
    """
    form = BookForm()
    init_book_form(form)
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
    return render_book_page(form, show_update_modal_on_error=True, update_book_id=book_id)
