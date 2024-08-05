-- The UNION ALL including the table_name as a column prior to the count will give us a list of all tables and their respective counts

SELECT 
    'jobs' AS table_name, 
    COUNT(*) AS table_count 
FROM 
    jobs
UNION ALL
SELECT 
    'unemployment' AS table_name, 
    COUNT(*) AS table_count 
FROM 
    unemployment
UNION ALL
SELECT 
    'employment' AS table_name, 
    COUNT(*) AS table_count 
FROM 
    employment
UNION ALL
SELECT 
    'income' AS table_name, 
    COUNT(*) AS table_count 
FROM 
    income
;