from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    publication_date = Column(Date, nullable=False)

    id_author = Column(Integer, ForeignKey("author.id",ondelete="CASCADE"))
    author = relationship("Author", back_populates="books")

    categories = relationship("Category", secondary="book_category", back_populates="books")