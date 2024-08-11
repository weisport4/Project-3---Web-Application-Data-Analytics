from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
import pandas as pd
import config as cfg

# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

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

    def full_data(self):
        query = """
                SELECT  
                    state.state,
                    year,
                    name,
                    latitude,
                    longitude,
                    tot_num_employed,
                    tot_num_unemployed,
                    tot_pctemp_agriculture,
                    tot_pctemp_mining,
                    tot_pctemp_construction,
                    tot_pctemp_manufacturing,
                    tot_pctemp_trade,
                    tot_pctemp_trans,
                    tot_pctemp_information,
                    tot_pctemp_fire,
                    tot_pctemp_services,
                    tot_pctemp_government,
                    tot_um_civ_labor_force
                FROM
                    (
                    SELECT
                        jobs.state,
                        employment.year,
                        sum(num_employed) as tot_num_employed,
                        sum(num_unemployed) as tot_num_unemployed,
                        sum(pctemp_agriculture) as tot_pctemp_agriculture,
                        sum(pctemp_mining) as tot_pctemp_mining,
                        sum(pctemp_construction) as tot_pctemp_construction,
                        sum(pctemp_manufacturing) as tot_pctemp_manufacturing,
                        sum(pctemp_trade) as tot_pctemp_trade,
                        sum(pctemp_trans) as tot_pctemp_trans,
                        sum(pctemp_information) as tot_pctemp_information,
                        sum(pctemp_fire) as tot_pctemp_fire,
                        sum(pctemp_services) as tot_pctemp_services,
                        sum(pctemp_government) as tot_pctemp_government,
                        sum(num_civ_labor_force) as tot_um_civ_labor_force
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
                        CAST(employment.year AS INTEGER) > 2010
                        AND jobs.state <> 'US'
                    GROUP BY
                        jobs.state, 
                        employment.year
                    ORDER BY 
                        jobs.state, 
                        employment.year
                    ) AS JOBS
                JOIN
                    state ON JOBS.state = state.state
                ORDER BY 
                    state, year desc
                """

        full_data_df = pd.read_sql(text(query), con=self.engine)
        data = full_data_df.to_dict(orient="records")
        return data

    def unemployment(self, year, state):
        query = f"""
                SELECT
                    state,
                    county,
                    sum(num_unemployed) as total_unemployed
                FROM
                    jobs
                JOIN
                   unemployment
                ON jobs.fips = unemployment.fips
                WHERE
                    CAST(unemployment.year AS INTEGER) = '{year}'
                    AND state = '{state}'
                GROUP BY
                    state,
                    county,
                    unemployment.year
                ORDER BY
                    total_unemployed desc
                ;
            """

        unemployment_df = pd.read_sql(text(query), con=self.engine)
        data = unemployment_df.to_dict(orient="records")
        return data

    def employment(self, year, state):
        query = f"""
                SELECT
                    state,
                    county,
                    sum(num_employed) as total_employed
                FROM
                    jobs
                JOIN
                   employment
                ON jobs.fips = employment.fips
                WHERE
                    CAST(employment.year AS INTEGER) = '{year}'
                    AND state = '{state}'
                GROUP BY
                    state,
                    county,
                    employment.year
                ORDER BY
                    total_employed desc
                ;
            """

        employment_df = pd.read_sql(text(query), con=self.engine)
        data = employment_df.to_dict(orient="records")
        return data