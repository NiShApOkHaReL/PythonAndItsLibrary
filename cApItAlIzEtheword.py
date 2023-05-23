'''str1 = input("Enter a string: ")
str2=
for i in range(0,len(str1)):
    if(i%2==0):
        str2[i]=str1[i].upper()
    else:
        str2[i] = str1[i]
    
print(str2)'''

str1 = input("Enter a string: ")
k = 0
for i in str1:
    if(k%2==0):
        i=i.upper()
        print(i,end = "")
    else:
        print(i,end="")
    k=k+1
