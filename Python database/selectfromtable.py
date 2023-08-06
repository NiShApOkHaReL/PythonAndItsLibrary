import mysql.connector as myconn
conn = myconn.connect(host="localhost",user="root",password="",database="utech") 

cursor=conn.cursor()

cursor.execute("SELECT * FROM student")

#myresult = cursor.fetchall()
myresult1 = cursor.fetchone()
print(myresult1)

#for x in myresult:
#  print(x)