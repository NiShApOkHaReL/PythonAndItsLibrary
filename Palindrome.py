# WAP to check whether a string is palindrome or not
str1 = input("Enter a string: ")
'''str2 = str1[::-1]
if(str1 == str2):
    print("Palindrome")
else:
    print("Not Palindrome")'''
    
for i in range(0,len(str1)):
    for j in range(-1,-len(str1),-1):
        if(str1[i] == str1[j]):
            continue
             if(i == len(str1)-1):
                 print("Palindrome")        
        else:
            break
        