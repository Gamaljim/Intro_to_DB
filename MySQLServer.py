import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='meloveyou2',
    )

    database_exists = False

    mycursor = mydb.cursor()
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')

    mycursor.close()
    mydb.close()

    print("Database 'alx_book_store' created successfully!")


except Error as e:
    print("Error Connecting to MYSQL")
