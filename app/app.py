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

@app.route("/api/v1.0/<econ_state>")
def get_data(econ_state):
    print(econ_state)

    # execute the queries
    data_map = sqlHelper.getStateData(econ_state)
    data_bar = sqlHelper.getUnemploymentData(econ_state)
    data_pie = sqlHelper.getEmploymentData(econ_state)
    data_pie2 = sqlHelper.getAllData(econ_state)

    data = {"state_data": data_map,
           "unemployment_data": data_bar,
           "employment_data": data_pie,
           "all_data": data_pie2}

    return jsonify(data)

#################################################
# Execute the App
#################################################
if __name__ == "__main__":
    app.run(debug=True)