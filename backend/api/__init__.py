from flask import Flask
from flask_cors import CORS
from database import db
from .config import environments

def setup_db(app, environment):
    app.config.from_object(environments[environment])
    db.app = app
    db.init_app(app)


def create_app(environment='dev'):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    setup_db(app, environment)
    CORS(app)
    return app



