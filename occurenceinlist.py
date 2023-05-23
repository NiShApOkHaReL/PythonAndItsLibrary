#WAP to count the frequency of a number in a list without using count function
li=eval(input("Enter the list elements: "))
a = int(input("WHich element do you want to count? "))
count = 0
for i in li:
    if(i==a):
        count = count+1
print(count)
    
