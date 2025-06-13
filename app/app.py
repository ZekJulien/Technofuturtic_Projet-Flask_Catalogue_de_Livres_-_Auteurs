import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .database import init_db
from .routes import blueprints

url_db = f"{os.getenv("SCHEME")}://{os.getenv("USERNAME_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOSTNAME")}:{os.getenv("PORT")}/{os.getenv("DATABASE_NAME")}"
print(url_db)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = url_db

csrf = CSRFProtect(app)
init_db(app)

for bp in blueprints:
    app.register_blueprint(bp)