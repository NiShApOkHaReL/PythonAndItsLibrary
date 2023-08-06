# Dictionary Methods/function
'''
len(), clear(), get(), items(), keys(), values(), update()'''
#Marks of three students "Suniti", "Ryna" and "Zeba" in three subjects are available in following three dictionaries respectively:
'''d1 = {1:40,2:70,3:70}
d2 = {1:40, 2:50, 3:60}
d3 = {1:70, 2:80, 3:90}
Create a nested dictionary that stores the marks details along with students names and then prints the output as shown below:'''
"""dict ={
    "Suniti":{1:40,2:70,3:70},"Ryna":{1:40, 2:50, 3:60},"Zeba":{1:70, 2:80, 3:90}
    }"""

'''
d1 = {1:40,2:70,3:70}
d2 = {1:40, 2:50, 3:60}
d3 = {1:70, 2:80, 3:90}

dict ={
    "Suniti":d1,"Ryna":d2,"Zeba":d3
    }'''
dict ={
    "Suniti":{1:40,2:70,3:70},"Ryna":{1:40, 2:50, 3:60},"Zeba":{1:70, 2:80, 3:90}
    }

for x in dict.keys():
    print("Name")
    print(x)
    print("Subject(key)","\t","Marks(values)")
    for y in dict[x].keys():
        print(" ",y,"\t\t",dict[x][y])
    print('\n')
   

