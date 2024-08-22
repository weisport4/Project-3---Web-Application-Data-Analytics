Project Overview:

This project focuses on developing a full-stack web application to visualize key job and income trends across rural America. The goal was to create an interactive dashboard featuring various data visualizations, including bar charts, sunburst charts, bubble charts, and a multi-layered map. The frontend involved data cleaning and analysis in Jupyter Notebook, preparing the dataset for insightful visualizations. On the backend, a PostgreSQL database was established using pgAdmin, with SQL queries executed to retrieve data for visualization. The final application, built with HTML, JavaScript, and VS Code, allows users to explore these visualizations and gain insights into the economic factors influencing rural America, showcasing the project's effective use of modern web technologies for data presentation.

App Interaction Instructions:

The website is relatively easy to use.
1.	Create the Economic Rural America database using pgAdmin4 (PostgreSQL).
2.	To create the tables, use economic_rural_america_atlas_database.sql, run that SQL in pgAdmin4 using the query tool while on the crowdfunding database.
3.	After running the Schema and creating the database, verify the tables were created by running the SQL in select_sql.sql. The counts will be zero as there is no data.
4.	Once the tables are created, run ETL_economic_rural_america_atlas.ipynb using Jupyter Notebook. This will create your database input .CSV files stored under DB_Input using the CSV input data under the resources directory.
5.	You will need to make sure you install psycopg2 in an anaconda prompt in the environment you are running the import. Use "conda install -c anaconda psycopg2" to install psycopg2.
6.	Prior to the next step copy the config.py file in the same location as you python code. The config.py will include the following, you will need to change the password to your PostgreSQL password: SQL_USERNAME = 'postgres' SQL_PASSWORD = '' SQL_IP = 'localhost' SQL_PORT = '5432' DATABASE = 'economic_rural_america_atlas'.
7.	Now that your database and input files are ready, you can load the data into the database using ETL_pandas_to_Postgres.ipynb in Jupyter Notebook.
8.	Run select_sql.sql again and you will get the row counts for each table.
9.	Once the tables are loaded, you can run the app. This will produce the website with the dashboard, visualizations, map and further pages.

Ethical Considerations:

In developing this full-stack web application to visualize job and income trends across rural America, ethical considerations were integral to every stage of the project. During the data cleaning and analysis phase, particular attention was paid to ensuring data accuracy and representation. Care was taken to represent the data fairly, avoiding any manipulations that could lead to misleading interpretations or biases, especially in areas affecting vulnerable rural populations. The interactive features of the dashboard were designed to present data transparently, enabling users to explore the visualizations without being subjected to any predetermined narratives. By prioritizing these ethical considerations, the project aimed to provide an honest, unbiased tool for understanding rural economic dynamics while respecting the communities represented in the data.

References:

chatGPT – used for debugging code and certain lines and blocks of code

Kaggle Dataset: Economic Atlas of Rural and Small-Town America (Kaggle - https://www.kaggle.com/datasets/davidbroberts/atlas-of-rural-and-smalltown-america) - Source of the dataset used for the project.

Xpert Learning Assistant

GitHub Repository: https://github.com/cisnerosjp/project3Team 2/tree/main - Served as a reference for project organization and structure.

Texas Tribune Article: https://www.texastribune.org/2023/11/21/texas-immigrants-pewresearch/#:~:text=Unauthorized%20immigrants%20make%20up%208,networks%20that%20encourage%20further%20immigration - Provided valuable context and background information related to immigration trends, which informed the broader narrative of the project.

USA Today Article: www.usatoday.com/story/news/politics/2023/06/21/florida-immigration-lawbusiness-owners-fear-exodus-of-workersconstruction-landscaping/703416320  - Offered insights into the impact of immigration policies on the workforce, contributing to the understanding of economic factors in rural areas.
