import mysql.connector as myconn
conn = myconn.connect(host="localhost",user="root",password="",database="utech") 

cursor=conn.cursor()

query='''UPDATE `student` SET `firstname`='Nisha' WHERE ID=1 '''

try:
    cursor.execute(query)
    
    conn.commit()
except:
    conn.rollback()
print("Table updated")
conn.close()
