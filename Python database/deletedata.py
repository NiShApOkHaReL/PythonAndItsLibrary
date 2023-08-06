import mysql.connector as myconn
conn = myconn.connect(host="localhost",user="root",password="",database="utech") 

cursor=conn.cursor()

query='''DELETE FROM student'''

try:
    cursor.execute(query)
    
    conn.commit()
except:
    conn.rollback()
print("Deleted")
conn.close()
