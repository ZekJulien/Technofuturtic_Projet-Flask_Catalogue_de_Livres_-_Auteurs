from app.repositories import AuthorRepository
from app.models import Author

class AuthorService:
    def __init__(self):
        self.author_repository = AuthorRepository()  

    def add_author(self, name: str, country: str | None = None):
        try:
            if not name:
                raise ValueError("Name cannot be empty.")
            if len(name) > 100:
                raise ValueError("Max lenght for name is 100.")
            new_author = Author(name=name)
            if country:
                new_author.country = country
                if len(country) > 100:
                    raise ValueError("Max lenght for name is 100.")
            return self.author_repository.add(new_author)
        except Exception as e:
            raise Exception(f"An unexpected error occurred while adding the author: {str(e)}")

    def get_all(self) -> list[Author]:
        try:
            return self.author_repository.get_all()
        except Exception as e:
            raise Exception(f"An unexpected error occurred while retrieving all authors: {str(e)}")
    
    def get_by_id(self, id : int) -> Author:
        try:
            return self.author_repository.get_by_id(id)
        except Exception as e:
            raise Exception(f"An unexpected error occurred while retrieving the author: {str(e)}")
    
    def delete(self, id : int) -> bool:
        try:
            author = self.get_by_id(id)
            if not isinstance(author, Author):
                raise Exception("Error: The provided ID does not exist")
            if self.author_repository.delete(author):
                return True
            raise Exception("Error: Failed to delete the author from the repository.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while deleting the author: {str(e)}")
