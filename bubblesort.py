# WAP to sort list element in ascending order using bubble sort algorithm.

li=eval(input("Enter the list: "))
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if(li[i]>li[j]):
            '''a = li[i]
            li[i]=li[j]
            li[j]=a'''
            li[i],li[j] = li[j],li[i] #Swapping
print(li)
    