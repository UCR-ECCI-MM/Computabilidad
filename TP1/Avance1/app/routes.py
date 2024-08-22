from flask import render_template
from flask import current_app as app

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/feature1.html', methods=['GET'])
def render_feature_1():
    return render_template("feature1.html")

@app.route('/feature2.html', methods=['GET'])
def render_feature_2():
    return render_template("feature2.html")

@app.route('/feature3.html', methods=['GET'])
def render_feature_3():
    return render_template("feature3.html")