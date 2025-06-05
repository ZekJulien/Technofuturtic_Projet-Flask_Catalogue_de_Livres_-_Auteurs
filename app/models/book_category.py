from sqlalchemy import Table, Column, ForeignKey
from .base import Base

book_category = Table(
    'book_category',
    Base.metadata,
    Column('id_book', ForeignKey('book.id', ondelete="CASCADE"), primary_key=True),
    Column('id_category', ForeignKey('category.id', ondelete="CASCADE"), primary_key=True)
)