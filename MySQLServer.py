import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='meloveyou2',
    database='alx_book_store'
)


database_exists = False

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')
mycursor.execute('SHOW DATABASES;')

for i in mycursor:
    if i == 'alx_book_store':
        database_exists = True
        break

mycursor.close()
mydb.close()

if database_exists:
    print("Database 'alx_book_store' created successfully!")
else:
    print("Database 'alx_book_store' was not found.")