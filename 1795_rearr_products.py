"""The module to make a request to MySQL database

Problem:
SWrite an SQL query to rearrange the Products table so that each row has (product_id, store, price). 
If a product is not available in a store, do not include a row with that product_id

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

Example: 
Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+

Link: https://leetcode.com/problems/rearrange-products-table/

"""


from getpass import getpass
from mysql.connector import connect, Error

#After starting MySQL server
connection = connect(
        host="localhost",
        user ='root',
        password="Server22$",
        #user=input("Enter username: "),
        #password=getpass("Enter password: "),
        database="leetdb"
)


cursor = connection.cursor()


#The name of the table for the challenge
table_name = "Products"

#cursor.execute(f"DROP TABLE {table_name}")

table_create = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    product_id INT PRIMARY KEY, 
    store1 INT, 
    store2 INT, 
    store3 INT
);
"""

insert_data = f"""
INSERT INTO {table_name} (product_id, store1, store2, store3)
VALUES
    ('0', '95', '100', '105'),
    ('1', '70', NULL, '80')
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
select 'store1' as store
  union all select 'store2'
  union all select 'store3'
from {table_name}
"""

solution2 = f"""
SELECT product_id, 'store1' as store, store1 as price
FROM {table_name}
WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' as store, store2 as price
FROM {table_name}
WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' as store, store3 as price
FROM {table_name}
WHERE store3 IS NOT NULL
ORDER BY product_id
"""

test_query = f"""
SELECT *
FROM {table_name}
"""


cursor.execute(solution2)
#cursor.execute(test_query)
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