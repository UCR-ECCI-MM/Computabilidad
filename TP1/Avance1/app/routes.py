from flask import render_template
from flask import current_app as app
import ast
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


""" EXAMPLE DATA """
dictionary = {}
with open("app/data/example.json", "r") as data:
    dictionary = ast.literal_eval(data.read())

# example data with  <information- category> tag counts.

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/feature1.html', methods=['GET'])
def render_feature_1():
    return render_template("feature1.html", json_data=dictionary)

@app.route('/feature2.html', methods=['GET'])
def render_feature_2():

    return render_template("feature2.html")

@app.route('/feature3.html', methods=['GET'])
def render_feature_3():
    return render_template("feature3.html")