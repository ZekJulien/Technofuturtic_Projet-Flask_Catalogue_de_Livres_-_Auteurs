import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import *

db = SQLAlchemy()

metadata = MetaData()

engine = create_engine(f"{os.getenv("SCHEME")}://{os.getenv("USERNAME_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOSTNAME_DB")}:{int(os.getenv("PORT"))}/{os.getenv("DATABASE_NAME")}")

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def init_db(app):
    try:
        db.init_app(app)
        #Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("✅ Database initialized successfully.")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")

def get_session():
    return Session()

