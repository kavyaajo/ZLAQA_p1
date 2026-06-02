#calculator app
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("1.add")
print('2.subtract')
print('3.multiply')
print('4.divide')
print('select operation:')
choice=int(input("Enter the choice:"))
num1=float(input("Enter the first no:"))
num2=float(input("Enter the second no:"))
if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice==3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice==4:
    if num2==0:
        print("Division by zero is not possible")
    else:
        print(f"{num1}/{num2}={div(num1,num2):.2f}")
else:
    print("Invalid input")

