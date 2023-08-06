print("Welcome to calculator")
num1=int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
n = int(input("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))

def addition():
    sum=num1+num2
    print("The sum is:",sum)
def subtration():
    sub = num1-num2
    print("The diff is: ",sub)
def mul():
    mul = num1*num2
    print("THe product is:",mul)

def div():
    try:
        div =num1/num2
        print("THe ans is ",div)    
    except:
        print("divisor cannot be zero, Divide by zero exception")



if(n==1):
    addition()
elif(n==2):
    subtraction()
elif(n==3):
    mul()
elif(n==4):
    div()
else:
    print("Invalid selection")