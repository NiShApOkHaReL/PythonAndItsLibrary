import mysql.connector as myconn
conn = myconn.connect(host="localhost",user="root",password="",database="utech") 

cursor=conn.cursor()

#query='''INSERT into student(ID,firstname,lastname,AGE,SEX) VALUES (1,"Garima", "Paudel",20,"Female")'''
#cursor.execute(query)
#conn.close()



insert_table= "INSERT into student(ID,firstname,lastname,AGE,SEX) VALUES (%s,%s,%s,%s,%s)"
data=[
    (3,"ABC", "Paudel",20,"Female"),
    (2,"Nisha", "Pokharel",22,"Female")
    ]



try:
    cursor.executemany(insert_table,data)
    conn.commit()
except:
    conn.rollback()
print("Data inserted")
conn.close()