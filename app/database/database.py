import os
import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import OperationalError
from app.models import *

db = SQLAlchemy()

metadata = MetaData()

engine = create_engine(f"{os.getenv("SCHEME")}://{os.getenv("USERNAME_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOSTNAME_DB")}:{int(os.getenv("PORT"))}/{os.getenv("DATABASE_NAME")}")

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def init_db(app):
    db.init_app(app)
    for i in range(5):
        try:
            Base.metadata.create_all(engine)
            print("✅ Database ready.")
            break
        except OperationalError as e:
            print(f"⏳ {i+1}/5 : DB not ready...")
            time.sleep(2)
    else:
        print("❌ Unable to connect to PostgreSQL after several attempts.")


def get_session():
    return Session()

