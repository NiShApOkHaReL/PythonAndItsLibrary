# WAP to create a dictonary containing names of competition winner students as keys and numbers of their wins as values.
num = int(input("Number of students: "))
d={}
for i in range(num):
    key = input("Enter the name of student: ")
    d[key] = int(input("Enter the no. of competition of wins: "))
    print(key,":",d[key])
print(d)