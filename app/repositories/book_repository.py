from .base_repository import BaseRepository
from app.models import Book

class BookRepository(BaseRepository[Book]):
    def __init__(self):
        super().__init__(Book)
    