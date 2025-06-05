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