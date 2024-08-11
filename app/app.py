from flask import Flask, jsonify
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route('/')
def welcome():
    return ('''
            Welcome to the Economic Atlas for Rural America and Small Towns API!                                                                                                            <br/>
            Available Routes:                                                                                                                                                              <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/full_data">/api/v1.0/full_data</a>                                                                                                  <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/unemployment/<year>/<state>">/api/v1.0/unemployment/<year>/<state></a>                                                                                            <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/employment/<year>/<state>">/api/v1.0/employment/<year>/<state></a>                                      
                            <br/>
            Explanation of the Routes:                                                                                                                                                      <br/>
            ''')

@app.route("/api/v1.0/full_data")
def full_data():
    data = sql.full_data()
    return jsonify(data)

@app.route("/api/v1.0/unemployment/<year>/<state>")
def unemployment(year, state):
    data = sql.unemployment(year, state)
    return jsonify(data)

@app.route("/api/v1.0/employment/<year>/<state>")
def employment(year, state):
    data = sql.employment(year, state)
    return jsonify(data)

# Run the App
if __name__ == '__main__':
    app.run(debug=True)