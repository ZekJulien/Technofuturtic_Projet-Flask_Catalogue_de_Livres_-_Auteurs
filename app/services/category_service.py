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
            raise Exception(f"An unexpected error occurred while adding the category: {str(e)}")
        
    def get_all(self) -> list[Category]:
        try:
            return self.category_repository.get_all()
        except Exception as e:
            raise Exception(f"An unexpected error occurred while retrieving all category: {str(e)}")
        
    def get_by_id(self, id : int) -> Category:
        try:
            return self.category_repository.get_by_id(id)
        except Exception as e:
            raise Exception(f"An unexpected error occurred while retrieving the category: {str(e)}")
    
    def delete(self, id : int) -> bool:
        try:
            category = self.category_repository.get_by_id(id)
            if not isinstance(category, Category):
                raise Exception("Error: The provided ID does not exist")
            if self.category_repository.delete(category):
                return True
            raise Exception("Error: Failed to delete the category from the repository.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred while deleting the category: {str(e)}")