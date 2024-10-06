"""This module contains all the webapp routes and feature processing."""

import base64
import json
from flask import render_template
from flask import current_app as app
from parser import parser
from parser import xml_dict
from .utilities import get_category_frequency,get_image_frequent_categories

# EXAMPLE DATA
dictionary = {}
with open("app/data/dataset.json", "r", encoding="utf8") as data:
    dictionary = json.loads(data.read())

#with open("data/mediplus_example.xml", "r", encoding='utf-8') as file:
with open("data/mplus_topics_2024-08-10(2).xml", "r", encoding='utf-8') as file:
    data = file.read()
    parser.parse(data)
#print(xml_dict)

frequent_category_plot_buffer = get_image_frequent_categories(get_category_frequency(xml_dict))


# Example data with  <information- category> tag counts:
inf_category_counts = {
    'Treatments and Therapies': 1000,
    'Patient Handouts': 900,
    'Encyclopedia': 600,
    'Start Here': 700,
    'Find an Expert': 800,
    'Reference Desk': 500,
    'Journal Articles': 400,
    'Symptoms': 100,
    'Health Check Tools': 300,
    'Related Issues': 200,
    'Learn More': 10, 
    'Find an expert': 40
}

@app.route('/', methods=['GET'])
def index():
    """Returns rendered root page."""
    return render_template("index.html")

@app.route('/feature1.html', methods=['GET'])
def render_feature_1():
    """Returns rendered feature1 page."""
    return render_template("feature1.html", json_data=dictionary)

@app.route('/feature2.html', methods=['GET'])
def render_feature_2():
    """Returns rendered feature2 page."""

    # Encode the image to base64 for embedding in HTML
    category_plot = base64.b64encode(frequent_category_plot_buffer.getvalue()).decode('utf8')

    # Render the template with the enbedding plot
    return render_template('feature2.html', category_plot=category_plot)

@app.route('/feature3.html', methods=['GET'])
def render_feature_3():
    """Returns rendered feature3 page."""
    return render_template("feature3.html",json_data=dictionary)
