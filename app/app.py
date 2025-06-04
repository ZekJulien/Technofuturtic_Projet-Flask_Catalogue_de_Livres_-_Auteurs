from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .config import SECRET_KEY, URL_DB
from .routes import blueprints
from .database import init_db

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB

csrf = CSRFProtect(app)

init_db(app)

for bp in blueprints:
    app.register_blueprint(bp)