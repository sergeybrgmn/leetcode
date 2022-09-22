"""The module to make a request to MySQL database

Problem:
Swap the enum values for one column 

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id is the primary key for this table.
The sex column is ENUM value of type ('m', 'f').
The table contains information about an employee.

SQL query to swap all 'f' and 'm' values 
(i.e., change all 'f' values to 'm' and vice versa) 
with a single update statement

Example: 
Input: 
Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+

Link: https://leetcode.com/problems/swap-salary/


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
table_name = "Salary"

#cursor.execute(f"DROP TABLE {table_name}")

table_create = f"""
CREATE TABLE IF NOT EXISTS {table_name}(
    id INT PRIMARY KEY, 
    name VARCHAR(100), 
    sex CHAR(1), 
    salary INT
);
"""

insert_data = f"""
INSERT INTO {table_name} (id, name, sex, salary)
VALUES
    ('1', 'A', 'm', 2500),
    ('2', 'B', 'f', 1500),
    ('3', 'C', 'm', 5500),
    ('4', 'D', 'f', 500)
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
UPDATE {table_name} SET sex = 
CASE 
    WHEN sex ='m' THEN 'f' 
    ELSE 'm' 
END;
"""

test_query = f"""
SELECT *
FROM {table_name}
"""
cursor.execute(solution_query)
connection.commit()

cursor.execute(test_query)
rows = cursor.fetchall()
#for desc in cursor.description:
#    print(desc[0], " | ", end = ' ')
#print(" ")   
for row in rows:
    print(row)
# Fetch rows from last executed query
#result = cursor.fetchall()
#for row in result:
#   print(row)