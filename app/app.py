# Import the dependencies.
from flask import Flask, jsonify, render_template
import pandas as pd
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper() # initialize the database helper

# Link for dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Link for info
@app.route("/")
def home_page():
    return render_template("info.html")

# Link for about us
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

# Link for links
@app.route("/links")
def links():
    return render_template("links.html")

# Link for state data
@app.route("/api/v1.0/stateData/<econ_state>")
def StateData(econ_state):
    state_data = sqlHelper.getstateData(econ_state)
    return (jsonify(state_data))

# Link for unemployment data
@app.route("/api/v1.0/unemploymentData/<econ_state>")
def UnemploymentData(econ_state):
    unemployment_data = sqlHelper.getUnemploymentData(econ_state)
    return (jsonify(unemployment_data))

# Link for employment data
@app.route("/api/v1.0/employmentData/<econ_state>")
def EmploymentData(econ_state):
    employment_data = sqlHelper.getEmploymentData(econ_state)
    return (jsonify(employment_data))

# Link for All Data data
@app.route("/api/v1.0/allData/<econ_state>")
def AllData(econ_state):
    all_data = sqlHelper.getAllData(econ_state)
    return (jsonify(all_data))


#################################################
# Execute the App
#################################################
if __name__ == "__main__":
    app.run(debug=True)