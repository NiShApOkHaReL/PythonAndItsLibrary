# WAP to calculate mean of a given list of numbers.

li=eval(input("Enter the list elements: "))
#li = [10,40,40]
l = len(li)
sum =0
for i in li:
    sum=sum + i
mean=sum/l
print(mean)