import mysql.connector as Myconn
mydb = Myconn.connect(host="localhost",user="root",password="")
print(mydb,"\nConnection Established.....")
