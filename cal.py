num1=float(input("enter your first number:"))
num2=float(input("enter your second number:"))
choice=input("enter your operator(+,-,*,/):")
result = None

if choice=="+":
    result=num1+num2
elif choice=="-":
    result=num1-num2
elif choice=="*":
    result=num1*num2 
elif choice=="/":
    if num2 !=0:
        result=num1/num2
    else:
        print("division by zero is not possible")     
else:
    print("invalid operator.")

if result is not None:
    print("result:",result)

