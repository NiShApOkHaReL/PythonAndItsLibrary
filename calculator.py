print("Welcome to Simple calculator")

choice = 1
while(choice ==1):
    a=int(input("1.Press 1 for addition of two numbers \n 2.Press 2 for subtraction of two numbers \n 3.Press 3 for multiplication of two numbers \n 4.Press 4 for division of two numbers \n"))
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    if(a==1):
        ans = num1+num2
        print(ans)
    elif(a==2):
        ans = num1-num2
        print("The diff is:", ans)
    elif(a==3):
        ans = num1*num2
        print("The produc is ", ans)
    elif(a==4):
        ans = num1/num2
        print("Ans is", ans)
    else:
        print("Invalid input")
    choice = int(input("Do you want to calculate again? 1 for yes and 0 for no"))