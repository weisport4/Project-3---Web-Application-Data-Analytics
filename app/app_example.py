# Import the dependencies.
from flask import Flask, jsonify, render_template
import pandas as pd
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper() # initialize the database helper

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/")
def home_page():
    return render_template("info.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/api/v1.0/<country>")
def get_data(country):
    print(country)

    # execute the queries
    data_map = sqlHelper.getMapData(country)
    data_bar = sqlHelper.getBarData(country)
    data_pie = sqlHelper.getPieData(country)
    data_pie2 = sqlHelper.getPieData2(country)

    data = {"map_data": data_map,
           "bar_data": data_bar,
           "pie_data": data_pie,
           "pie_data2": data_pie2}

    return jsonify(data)

#################################################
# Execute the App
#################################################
if __name__ == "__main__":
    app.run(debug=True)