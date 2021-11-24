import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='123456',
                              host='127.0.0.1',
                              database='shop')
cursor = cnx.cursor()
cursor.execute("SELECT * from products")

for data in cursor:
    print(data) 

cnx.close()