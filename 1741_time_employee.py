"""The module to make a request to MySQL database

Problem:
Find Total Time Spent by Each Employee

The table shows the employees' entries and exits in an office.
- event_day is the day at which this event happened, 
- in_time is the minute at which the employee entered the office, 
- out_time is the minute at which they left the office.


calculate the total time in minutes spent by each employee on each day at the office. 
within one day, an employee can enter and leave more than once. 
The time spent in the office for a single entry is out_time - in_time

+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+

Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee/


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

#cursor.execute("DROP TABLE Employees")

table_create = """
CREATE TABLE IF NOT EXISTS Employees(
    emp_id INT, 
    event_day DATE, 
    in_time INT, 
    out_time INT
);
"""

insert_data = """
INSERT INTO Employees (emp_id, event_day, in_time, out_time)
VALUES
    ('1', '2020-11-28', '4', '32'),
    ('1', '2020-11-28', '55', '200'),
    ('1', '2020-12-3', '1', '42'),
    ('2', '2020-11-28', '3', '33'),
    ('2', '2020-12-9', '47', '74')
"""

#create table
cursor.execute(table_create)
connection.commit()

#truncate to keep constant initial data
cursor.execute("TRUNCATE TABLE Employees")

#insert data
cursor.execute(insert_data)
connection.commit()

#solution query
solution_query = """
SELECT 
    event_day as day, 
    emp_id as emp_id, 
    sum(out_time - in_time) as total_time
FROM Employees
GROUP BY event_day, emp_id
ORDER BY event_day
"""

#The name of the table for the challenge
table_name = "Employees"
test_query = f"""
SELECT *
FROM {table_name}
"""
#cursor.execute(test_query)
cursor.execute(solution_query)
rows = cursor.fetchall()
for desc in cursor.description:
    print(desc[0], " | ", end = ' ')
print(" ")   
for row in rows:
    print(row)
# Fetch rows from last executed query
#result = cursor.fetchall()
#for row in result:
#   print(row)