from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from app.config import URL_DB
from app.models import Base

db = SQLAlchemy()

metadata = MetaData()

engine = create_engine(URL_DB)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def init_db(app):
    try:
        db.init_app(app)
        Base.metadata.create_all(engine)
        print("✅ Database initialized successfully.")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")

def get_session():
    return Session()

