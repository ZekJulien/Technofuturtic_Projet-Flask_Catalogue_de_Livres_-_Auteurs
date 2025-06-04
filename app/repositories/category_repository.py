from app.models import Category
from app.repositories import BaseRepository

class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(Category)

