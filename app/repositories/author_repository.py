from app.models import Author
from app.repositories import BaseRepository

class AuthorRepository(BaseRepository[Author]):
    def __init__(self):
        super().__init__(Author)

