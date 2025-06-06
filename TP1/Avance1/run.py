"""
This is the starting point for the whole program.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=3000, debug=False)
