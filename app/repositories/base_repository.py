from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from app.database import get_session
from sqlalchemy.orm import declarative_base

T = TypeVar("T", bound=declarative_base)

class BaseRepository(Generic[T]):
    model: T

    def __init__(self, model: T):
        self.model = model

    def add(self, entity : T) -> T:
        with get_session() as session:
            session.add(entity)
            session.commit()
            return entity
        
    def get_all(self) -> list[T]:
        with get_session() as session:
            return session.query(self.model).all()
        
    def get_by_id(self, id : int) -> T:
        with get_session() as session:
            return session.query(self.model).filter(self.model.id == id).first()
        
    def delete(self, entity : T):
        with get_session() as session:
            session.delete(entity)
            session.commit()
            return True