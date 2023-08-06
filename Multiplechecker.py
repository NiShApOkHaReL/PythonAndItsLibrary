a = int(input("Enter the number: "))
for i in range(a):
    b=i+1
    if(b==1):
        print(b)
    elif(b%3==0 and b%5==0):
        print("Multiple of both 3 and 5")
    elif(b%3==0):
        print("Multiple of 3")
    elif(b%5==0):
        print("Multiple of 5")
    
    else:
        print(b)
  '''      
a = int(input())
for i in range(a):
    b=i+1
    if(b==1):
        print(b)
    elif(b%3==0 and b%5==0):
        print("FizzBuzz")
    elif(b%3==0):
        print("Fizz")
    elif(b%5==0):
        print("Buzz")
    else:
        print(b)'''
        
        
