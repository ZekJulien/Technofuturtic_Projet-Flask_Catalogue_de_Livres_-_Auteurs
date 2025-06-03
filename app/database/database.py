from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from app.config import URL_DB

db = SQLAlchemy()

metadata = MetaData()

engine = create_engine(URL_DB)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def get_session():
    return Session()
