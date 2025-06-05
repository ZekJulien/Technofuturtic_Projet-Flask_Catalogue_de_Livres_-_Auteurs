from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=True)

    books = relationship("Book", back_populates="author")