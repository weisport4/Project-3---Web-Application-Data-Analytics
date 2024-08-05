# Project-3---Web-Application-Data-Analytics
Web Application with Data Analytics using Flask

# Economic Rural Atlas America
Project Overview
This project involves creating an economic rural atlas America database. It is divided into these steps:

.......

Steps to run the application:
    A. Create the Economic Rural America database using pgAdmin4 (postgres)
    B. To create the tables use economic_rural_america_atlas_database.sql, run that SQL in pgAdmin4 using the query tool while on the crowdfunding database
    C. After running the Schema and creating the database, verify the tables were created by running the SQL in select_sql.sql.  The counts will be zero as their is no data.
    D. Once the tables are created, run ETL_economic_rural_america_atlas.ipynb using jupyter notebook.  This will create your database input .CSV files stored  under DB_Input using the CSV input data under the resources directory.
    E. You will need to make sure you install psycopg2 in an anaconda prompt in the environment you are running the import.  Use "conda install -c anaconda psycopg2" to install psycopg2.
    F. Prior to the next step copy the config.py file in the same location as you python code. The config.py will include the following, you will need to change the password to you postgres password:
        SQL_USERNAME = 'postgres'
        SQL_PASSWORD = '<YOUR PASSWORD>'
        SQL_IP = 'localhost'
        SQL_PORT = '5432'
        DATABASE = 'economic_rural_america_atlas'
    H. Now that your database and input files are ready, you can load the data into the database using ETL_pandas_to_Postgres.ipynb in jupyter notebook
    I. Run select_sql.sql again and you will get the row counts for each table.
    J. Once the tables are loaded, you can run ????????????.  This will produce the website with the dashboard, visualizations, map and further pages