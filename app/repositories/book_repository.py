from .base_repository import BaseRepository
from app.models import Book
from sqlalchemy.orm import joinedload
from app.database import get_session

class BookRepository(BaseRepository[Book]):
    def __init__(self):
        super().__init__(Book)
    
    def get_all(self) -> list[Book]:
        with get_session() as session:
            return session.query(Book).options(joinedload(Book.categories)).all()
        
    def get_by_id(self, id : int) -> Book:
        with get_session() as session:
            return session.query(self.model).options(joinedload(Book.categories)).filter(self.model.id == id).first()