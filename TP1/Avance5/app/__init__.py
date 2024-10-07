"""
Creates and configures flask app. Uses the factory design pattern.
"""
from flask import Flask
import sys

def create_app():
    """Returns a flask app"""
    try:
        app = Flask(__name__)
        app.jinja_env.trim_blocks = True
        app.jinja_env.lstrip_blocks = True
        with app.app_context():
            from . import routes
    except SyntaxError as e:
        print(f"{e}\nServer stopped.")
        sys.exit(1)  # Stop the server with exit code 1
    except Exception as e:
        print(f"Error creating the application: {e}")
        sys.exit(1)  # Stop the server with exit code 1
    return app
    
