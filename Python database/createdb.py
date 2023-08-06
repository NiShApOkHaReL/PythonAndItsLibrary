import mysql.connector as mycon
conn = mycon.connect(host="localhost", user="root", password="", database="utech")

cursor = conn.cursor()
cursor.execute("Drop database if exists utech")
sql = "create database utech"
cursor.execute(sql)
print("List of databases: ")
cursor.execute("show databases")
print(cursor.fetchall())
conn.close()
