from flask import render_template
from flask import current_app as app

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
