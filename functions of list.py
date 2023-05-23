#List methods in python
# len() , count(), extend(), insert(), remove(), pop(), del, clear(), sort(),
'''li = [10,40,40]
print(len(li))
print(li.count(40))
li.append(50)
print(li)
li.extend([60,70])
print(li)
li.insert(1,90)
print(li)
li.pop(1)
print(li)
del li[0:3]
li.clear()'''

li1 = [1,5,4,3,2,3]
li1.sort()  #ascending
print(li1)
li1.sort(reverse=True)  #descending
print(li1)
print(li1.index(3))
