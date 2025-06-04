from app.repositories import AuthorRepository
from app.models import Author

class AuthorService:
    def __init__(self):
        self.author_repository = AuthorRepository()  

    def add_author(self, name: str, country: str | None = None):
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
