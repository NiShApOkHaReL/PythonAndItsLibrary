import mysql.connector as myconn

conn= myconn.connect(host="localhost",user="root",password="",database="utech")
cursor = conn.cursor()

query='''CREATE table student(ID INT PRIMARY KEY,firstname CHAR(20) NOT NULL,lastname CHAR(20),AGE INT, SEX CHAR(1))'''
cursor.execute(query)
conn.close()

