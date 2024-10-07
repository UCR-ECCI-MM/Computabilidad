"""This module contains all the webapp routes and feature processing."""

import base64
import json
from io import BytesIO
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

"""
We generate the plot once per server execution. The `10 most frequent categories` plot 
is saved to a BytesIO buffer.
"""
frequent_category_plot_buffer = get_image_frequent_categories(get_category_frequency(xml_dict))


@app.route('/', methods=['GET'])
def index():
    """Returns rendered root page."""
    return render_template("index.html", date=xml_dict['date_created'], 
                           time=xml_dict['time_created'], 
                           counts=xml_dict['total'])

@app.route('/feature1.html', methods=['GET'])
def render_feature_1():
    """Returns rendered feature1 page."""
    #return render_template("feature1.html", json_data=dictionary)
    return render_template("feature1.html", json_data= {'health_topics' : xml_dict['health_topics'][0:50]})

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
