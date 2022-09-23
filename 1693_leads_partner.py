"""The module to make a request to MySQL database

Problem:
Data grouping

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| date_id     | date    |
| make_name   | varchar |
| lead_id     | int     |
| partner_id  | int     |
+-------------+---------+
This table does not have a primary key.
This table contains the date and the name of the product sold and the IDs of the lead and partner it was sold to.
The name consists of only lowercase English letters.

Write an SQL query that will, 
for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.

Input: 
DailySales table:
+-----------+-----------+---------+------------+
| date_id   | make_name | lead_id | partner_id |
+-----------+-----------+---------+------------+
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |
+-----------+-----------+---------+------------+
Output: 
+-----------+-----------+--------------+-----------------+
| date_id   | make_name | unique_leads | unique_partners |
+-----------+-----------+--------------+-----------------+
| 2020-12-8 | toyota    | 2            | 3               |
| 2020-12-7 | toyota    | 1            | 2               |
| 2020-12-8 | honda     | 2            | 2               |
| 2020-12-7 | honda     | 3            | 2               |
+-----------+-----------+--------------+-----------------+


Link: https://leetcode.com/problems/daily-leads-and-partners/

"""


from getpass import getpass
from mysql.connector import connect, Error

#After starting MySQL server
connection = connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="leetdb"
)


cursor = connection.cursor()


#The name of the table for the challenge
table_name = "DailySales"

#cursor.execute(f"DROP TABLE {table_name}")


table_create = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    date_id DATE,
    make_name VARCHAR(20),
    lead_id INT,
    partner_id INT
);
"""

insert_data = f"""
INSERT INTO {table_name} (date_id, make_name, lead_id, partner_id)
VALUES
('2020-12-8', 'toyota', '0', '1'),
('2020-12-8', 'toyota', '1', '0'),
('2020-12-8', 'toyota', '1', '2'),
('2020-12-7', 'toyota', '0', '2'),
('2020-12-7', 'toyota', '0', '1'),
('2020-12-8', 'honda', '1', '2'),
('2020-12-8', 'honda', '2', '1'),
('2020-12-7', 'honda', '0', '1'),
('2020-12-7', 'honda', '1', '2'),
('2020-12-7', 'honda', '2', '1')
"""

#create table
cursor.execute(table_create)
connection.commit()

#truncate to keep constant initial data
cursor.execute(f"TRUNCATE TABLE {table_name}")

#insert data
cursor.execute(insert_data)
connection.commit()

#solution query
solution_query = f"""
SELECT
    date_id, 
    make_name, 
    COUNT(DISTINCT(lead_id)) as unique_leads,
    COUNT(DISTINCT(partner_id)) as unique_partners
FROM {table_name}
GROUP BY date_id,make_name
ORDER BY make_name DESC, date_id DESC 
"""

test_query = f"""
SELECT *
FROM {table_name}
"""


#cursor.execute(solution2)
cursor.execute(solution_query)
rows = cursor.fetchall()
print("-" * 60) 
for desc in cursor.description:
    print(desc[0], " | ", end = ' ')
print(" ")
print("-" * 60)   
for row in rows:
    for col in row:
        print(f"{col} |", end=' ')
    print("|")
# Fetch rows from last executed query
#result = cursor.fetchall()
#for row in result:
#   print(row)