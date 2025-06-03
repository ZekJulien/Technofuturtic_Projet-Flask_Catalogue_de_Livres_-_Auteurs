from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .config import SECRET_KEY, URL_DB
from .database import db, engine

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB

csrf = CSRFProtect(app)

try:
    db.init_app(app)
    print("✅ Database initialized successfully!")
except Exception as e:
    print(f"🛑 Database initialization failed:\n{e}")
