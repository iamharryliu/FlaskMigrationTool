from WebApp.config import Config
from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index_redirect():
        return redirect("http://localhost:5000/admin")

    @app.route("/<wildcard>")
    def wilcard_redirect(wildcard):
        return redirect("http://localhost:5000/admin")

    from WebApp.models import User

    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))

    return app
