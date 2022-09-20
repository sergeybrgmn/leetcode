"""The module to make a request to MySQL database

Easy problem. 
The pipline to work with MySQL server was created:
- leetdb database on the MySQL Server
- establishing connection to the database
- input initial table and insert data
- solution query

Link: https://leetcode.com/problems/recyclable-and-low-fat-products/

"""


from getpass import getpass
from mysql.connector import connect, Error


"""
#Create new database to store all the tables
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE leetdb"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

"""
#After starting MySQL server
connection = connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="leetdb"
)


#with open('tables.sql', 'r') as sql_file:
#    sql_script = sql_file.read()

cursor = connection.cursor()

#cursor.execute(sql_script)
#connection.commit()

table_create = """
CREATE TABLE IF NOT EXISTS Products(
    product_id INT PRIMARY KEY,
    low_fats ENUM('Y', 'N'),
    recyclable ENUM('Y','N')
);
"""

insert_data = """
INSERT INTO Products (product_id, low_fats, recyclable)
VALUES
    (0, 'Y', 'N'),
    (1, 'Y', 'Y'),
    (2, 'N', 'Y'),
    (3, 'Y', 'Y'),
    (4, 'N', 'N')
"""

#create table
cursor.execute(table_create)
connection.commit()

#truncate to keep constant initial data
cursor.execute("TRUNCATE TABLE Products")

#insert data
cursor.execute(insert_data)
connection.commit()

#solution query
solution_query = """
SELECT product_id 
FROM Products as p
WHERE p.low_fats = "Y"
AND p.recyclable = "Y"
"""

cursor.execute(solution_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
# Fetch rows from last executed query
#result = cursor.fetchall()
#for row in result:
#   print(row)