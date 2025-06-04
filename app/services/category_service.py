from app.repositories import CategoryRepository
from app.models import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()  

    def add_category(self, name : str):
        try:
            if not name:
                raise ValueError("Name cannot be empty.")
            if len(name) > 100:
                raise ValueError("Max lenght for name is 100.")
            new_category = Category(name=name)
            return self.category_repository.add(new_category)
        except Exception as e:
            raise Exception(f"An unexpected error occurred while adding the author: {str(e)}")