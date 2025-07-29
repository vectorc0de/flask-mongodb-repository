
from flask import Flask
from flask_mongoengine import MongoEngine
from .config import Config

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
