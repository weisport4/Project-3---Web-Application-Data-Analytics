from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func, case
import pandas as pd
import datetime as dt
import config as cfg



# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        # Setup the Postgres connection variables
        SQL_USERNAME = cfg.SQL_USERNAME
        SQL_PASSWORD = cfg.SQL_PASSWORD
        SQL_IP = cfg.SQL_IP
        SQL_PORT = cfg.SQL_PORT
        DATABASE = cfg.DATABASE

        connection_string = f'postgresql+psycopg2://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_IP}:{SQL_PORT}/{DATABASE}'
        # Connect to PostgreSQL server
        self.engine = create_engine(connection_string)
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def full_data_sql(self):
        # Find the most recent date in the data set.
        query = """
                SELECT
                    	state,
                        county,
            			employment.year,
            			num_employed,
            			num_unemployed,
                        pctemp_agriculture,
                        pctemp_mining,
                        pctemp_construction,
                        pctemp_manufacturing,
                        pctemp_trade,
                        pctemp_trans,
                        pctemp_information,
                        pctemp_fire,
                        pctemp_services,
                        pctemp_government,
                        num_civ_labor_force
            FROM
                jobs
            JOIN
                employment
                ON jobs.fips = employment.fips
            JOIN
                unemployment
                ON employment.fips = unemployment.fips
                AND employment.year = unemployment.year
            WHERE
                CAST(employment.year AS INTEGER) > 2014
            	and state <> 'US'
            ORDER BY 
                jobs.state, jobs.county, employment.year
		;
                ;
                """

        # Save the query results as a Pandas DataFrame
        income_data_sql_df = pd.read_sql(text(query), con=self.engine)
        data = income_data_sql_df.to_dict(orient="records")
        return (data)
