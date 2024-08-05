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
            Welcome to the Economic Atlas for Rural America and small towsn API!                                                                                                            <br/>
            Available Routes:                                                                                                                                                               <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/full_data_sql">/api/v1.0/income_sql</a>                                                                                              <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/reached_goal_sql">/api/v1.0/jobs_sql</a>                                                                                             <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/count_of_categories_by_outcome_sql">/api/v1.0/unemployment_sql</a>                                                                   <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;<a href="/api/v1.0/count_of_subcategories_by_outcome_sql">/api/v1.0/employment_sql</a>                                                                  <br/>
                                                                                                                                                                                            <br/>
                                                                                                                                                                                            <br/>
            Explanation of the Routes:                                                                                                                                                      <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;full_data_sql: Returns all the data from the income table using SQL.                                                                                    <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;reached_goal_sql: Returns the jobs data from the jobs table using SQL.
                            <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;reached_goal_sql: Returns the unemployment data from the unemployment table using SQL.
                            <br/>
            &nbsp;&nbsp;&nbsp;&nbsp;reached_goal_sql: Returns the employment data from the employment table using SQL.
                            <br/>
            ''')


@app.route("/api/v1.0/income_data_sql")
def income_data_sql():
    data = sql.income_data_sql()
    return (jsonify(data))


@app.route("/api/v1.0/jobs_data_sql")
def jobs_data_sql():
    data = sql.jobs_data_sql()
    return (jsonify(data))


@app.route("/api/v1.0/unemployment_data_sql")
def unemployment_data_sql():
    data = sql.unemployment_data_sql()
    return (jsonify(data))

@app.route("/api/v1.0/employment_data_sql")
def employment_data_sql():
    data = sql.employment_data_sql()
    return (jsonify(data))



@app.route("/api/v1.0/count_of_categories_by_outcome_orm")
def count_of_categories_by_outcome_orm():
    data = sql.count_of_categories_by_outcome_orm()
    return (jsonify(data))

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
