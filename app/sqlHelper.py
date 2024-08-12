import sqlalchemy
from sqlalchemy import create_engine, func, inspect, text
import pandas as pd

class SQLHelper():

    def __init__(self):
        self.engine = create_engine("sqlite:///resources/AQI and Lat Long of Countries.sqlite")

    def getstateData(self, econ_state):
        # allow the user to select ALL country
        if econ_state == "All":
            where_clause = f"econ_state <> 'US'"
        else:
            where_clause = f"econ_state = '{state}'"

        query = f"""
                SELECT
                    econ_state,
                    latitude,
                    longitude,
                    name
                FROM
                    state
                WHERE
                    {where_clause};
        """

        state_df = pd.read_sql(text(query), con=self.engine)
        data_map = state_df.to_dict(orient="records")

        return(data_map)
    
    def getUnemploymentData(self, econ_state):
        # allow the user to select ALL states
        if Year == "All":
            where_clause = f"econ_state <> 'US'"
        else:
            where_clause = f"j.econ_state = '{econ_state}'"
        query = f"""
                SELECT
                    u.econ_state,
                    u.econ_year,
                    s.name AS state_name,
                    s.latitude,
                    s.longitude,
                    COALESCE(u.tot_num_unemployed, 0) AS total_unemployed
                FROM
                    (
                    SELECT
                        j.econ_state,
                        u.econ_year,
                        SUM(u.num_unemployed) AS tot_num_unemployed
                    FROM
                        unemployment u
                    JOIN
                        jobs j
                    ON u.fips = j.fips
                    WHERE
                        {where_clause};
                    GROUP BY
                        j.econ_state, u.econ_year
                    ) AS u
                JOIN
                    state s
                ON u.econ_state = s.econ_state
                ORDER BY
                    u.econ_state, u.econ_year;
                """

        unemployment_df = pd.read_sql(text(query), con=self.engine)
        data_bar = unemployment_df.to_dict(orient="records")

        return(employment_data)
    
    def getEmploymenteData(self, econ_state):
        # allow the user to select ALL country
        if econ_state == "All":
            where_clause = f"econ_state <> 'US'"
        else:
            where_clause = f"j.econ_state = '{econ_state}'"

        query = f"""
                SELECT
                    e.econ_state,
                    e.econ_year,
                    s.name AS state_name,
                    s.latitude,
                    s.longitude,
                    COALESCE(e.tot_num_employed, 0) AS total_employed
                FROM
                    (
                    SELECT
                        j.econ_state,
                        e.econ_year,
                        SUM(e.num_employed) AS tot_num_employed
                    FROM
                        employment e
                    JOIN
                        jobs j
                    ON e.fips = j.fips
                    WHERE
                        {where_clause};
                    GROUP BY
                        j.econ_state, e.econ_year
                    ) AS e
                JOIN
                    state s
                ON e.econ_state = s.econ_state
                ORDER BY
                    e.econ_state, e.econ_year;
                """

        employment_df = pd.read_sql(text(query), con=self.engine)
        data_pie = employment_df.to_dict(orient="records")

        return(unemployment_data)
    
    def getAllData(self, econ_state):
        # allow the user to select ALL country
        if econ_state == "All":
            where_clause = f"econ_state <> 'US'"
        else:
            where_clause = f"econ_ = '{econ_state}'"

        query = f"""
                SELECT state.econ_state,
                        econ_year,
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
                        jobs.econ_state,
                        employment.econ_year,
                        sum(num_employed) as tot_num_employed,
                        sum(num_unemployed) as tot_num_unemployed,
                        sum(pctemp_agriculture) as tot_pctemp_agriculture,
                        sum(pctemp_mining)as tot_pctemp_mining,
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
                    AND employment.econ_year = unemployment.econ_year
                    WHERE
                        jobs.econ_state <> 'US'
                    GROUP BY
                        jobs.econ_state,
                        employment.econ_year
                    ORDER BY
                        jobs.econ_state,
                        employment.econ_year
                    ) AS JOBS
                JOIN
                    state ON JOBS.econ_state = state.econ_state
                ORDER BY
                    econ_state,
                    econ_year
        """

        alldata_df = pd.read_sql(text(query), con=self.engine)
        data_pie2 = alldata_df.to_dict(orient="records")

        return(data_pie2)