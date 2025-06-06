from app.repositories import BookRepository, AuthorRepository, CategoryRepository
from app.models import Book, Author, Category
from datetime import date

class BookService:
    def __init__(self):
        self.book_repository : BookRepository = BookRepository()
        self.author_repository : AuthorRepository = AuthorRepository()
        self.category_repository : CategoryRepository = CategoryRepository()

    def add_book(self, title : str, genre : str, publication_date : date, id_author : int, category_ids : list[int]):
        try:
            if self._check_book_value(title=title, genre=genre, publication_date=publication_date, id_author=id_author):
                categories : list[Category] = []
                for id in category_ids:
                    categories.append(self.category_repository.get_by_id(id))
                        
                self.book_repository.add(Book(
                    title=title,
                    genre=genre,
                    publication_date=publication_date,
                    id_author=id_author,
                    categories = categories
                ))
        except Exception as e:
            raise Exception(f"An unexpected error occurred while adding the book: {str(e)}")
        
    def get_all(self) -> list[Book]:
        return self.book_repository.get_all()
    
    def delete(self, id : int) -> bool:
        try:
            book = self.book_repository.get_by_id(id)
            if not isinstance(book, Book):
                raise Exception("Error: The provided ID does not exist")
            if self.book_repository.delete(book):
                return True
            raise Exception("Error: Failed to delete the book from the repository.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while deleting the book: {str(e)}")
      
    def update(self, id : int, title : str, genre : str, publication_date : date, id_author : int, category_ids : list[int]):
        try:
            if self._check_book_value(title=title, genre=genre, publication_date=publication_date, id_author=id_author):
                db_book = self.book_repository.get_by_id(id)
                if isinstance(db_book, Book):    
                    categories : list[Category] = []
                    for id in category_ids:
                        categories.append(self.category_repository.get_by_id(id))

                    
                    db_book.title= title or db_book.title
                    db_book.genre= genre or db_book.genre
                    db_book.publication_date= publication_date or db_book.publication_date
                    db_book.id_author= id_author or db_book.id_author
                    db_book.categories = categories or db_book.categories
                    
                    if self.book_repository.update(db_book):
                        return True
        except Exception as e:
            raise Exception(f"An unexpected error occurred while updating the book: {str(e)}")

        
    def _check_book_value(self, title : str, genre : str, publication_date : date, id_author : int):
        if not title:
            raise ValueError("Title cannot be empty.")
        if len(title) > 100:
            raise ValueError("Max lenght for title is 100.")
        if not genre:
            raise ValueError("Genre cannot be empty.")
        if len(genre) > 100:
            raise ValueError("Max lenght for genre is 100.")
        if not publication_date:
            raise ValueError("Publication date cannot be empty.")
        if not id_author:
            raise ValueError("Author cannot be empty.")
        author = self.author_repository.get_by_id(id_author)
        if not isinstance(author, Author):
            raise Exception("Author does not exist.")
        return True