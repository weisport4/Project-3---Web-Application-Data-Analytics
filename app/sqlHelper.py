from sqlalchemy import text
import pandas as pd

class SQLHelper:
    # Initialization and setup methods remain unchanged

    def full_data(self):
        query = text("""
            SELECT  
                state.econ_state,
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
                AND employment.econ_year = unemployment.econ_year
                WHERE
                    CAST(employment.econ_year AS INTEGER) > :year_threshold
                    AND jobs.econ_state <> 'US'
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
                econ_state, econ_year desc
        """)
        full_data_df = pd.read_sql(query, con=self.engine, params={"year_threshold": 2010})
        data = full_data_df.to_dict(orient="records")
        return data

    def unemployment(self, year, state):
        query = text("""
            SELECT
                econ_state,
                sum(num_unemployed) as total_unemployed
            FROM
                jobs
            JOIN
               unemployment
            ON jobs.fips = unemployment.fips
            WHERE
                CAST(unemployment.econ_year AS INTEGER) = :year
                AND econ_state = :state
            GROUP BY
                econ_state,
                county,
                unemployment.econ_year
            ORDER BY
                total_unemployed desc
        """)
        unemployment_df = pd.read_sql(query, con=self.engine, params={"year": year, "state": state})
        data = unemployment_df.to_dict(orient="records")
        return data

    def employment(self, year, state):
        query = text("""
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
                CAST(employment.year AS INTEGER) = :year
                AND state = :state
            GROUP BY
                state,
                county,
                employment.year
            ORDER BY
                total_employed desc
        """)
        employment_df = pd.read_sql(query, con=self.engine, params={"year": year, "state": state})
        data = employment_df.to_dict(orient="records")
        return data
