# WAp to find the maximum element of a list with it's index.
li1 = eval(input("Enter the list: "))

max = li1[0]
for i in li1:
    if(i>max):
        max = i
    
print("The maximum element is: ", max)
print("The index is: ",li1.index(max))