#Simple Calculator Using Python

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


print("start operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    numbers = input("enter numbers(1/2/3/4/):")
    if numbers in ('1','2','3','4'):
        num1 = float(input("enter first number:"))
        num2 = float(input("enter second number:"))
    if numbers == '1':
        print(num1,"+",num2,"=",add(num1,num2))

    elif numbers == '2':
        print(num1,"-",num2,"=",subtract(num1,num2))

    elif numbers == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif numbers == '4':
        print(num1, "/", num2, "=", divide(num1, num2))




    else:
        print("invalid input")



