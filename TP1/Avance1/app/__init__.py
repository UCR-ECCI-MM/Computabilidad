"""
Creates and configures flask app. Uses the factory design pattern.
"""
from flask import Flask

def create_app():
    """Returns a flask app"""
    app = Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    with app.app_context():
        from . import routes
    return app
