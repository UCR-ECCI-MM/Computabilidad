from flask import render_template
from flask import current_app as app
import ast
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
import json

""" EXAMPLE DATA """
dictionary = {}
with open("app/data/dataset.json", "r") as data:
    dictionary = json.loads(data.read())

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
    return render_template("index.html")

@app.route('/feature1.html', methods=['GET'])
def render_feature_1():
    return render_template("feature1.html", json_data=dictionary)

@app.route('/feature2.html', methods=['GET'])
def render_feature_2():
    # cast the `inf_category_counts` dictionary to a dataFrame
    df_category_counts = pd.DataFrame(list(inf_category_counts.items()), columns=['Category', 'Count'])
    # get the 10 most popular categories
    popular_category_counts = df_category_counts.sort_values(by='Count', ascending=False).head(10)

    # create a horizontal barplot
    #plt.figure(figsize=(2, 4))
    plt.figure(figsize=(6, 6))
    sns.barplot(x='Count', y='Category', data=popular_category_counts, orient='h')
    #plt.title('10 Most Popular Information Categories')
    plt.xlabel('Count')
    plt.ylabel('Category')
    plt.tight_layout() 

    # save the barplot to a temporary buffer 
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    #buffer.seek(0)

    # Encode the image to base64 for embedding in HTML
    category_plot = base64.b64encode(buffer.getvalue()).decode('utf8')
    plt.close()

    # Render the template with the enbedding plot
    return render_template('feature2.html', category_plot=category_plot)

@app.route('/feature3.html', methods=['GET'])
def render_feature_3():
    return render_template("feature3.html",json_data=dictionary)