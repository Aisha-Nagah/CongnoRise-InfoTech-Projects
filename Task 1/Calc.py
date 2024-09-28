# Simple Calculator App
#Aisha Nagah

def calculator():
    print("Welcome to the Calculator App")
    
    num1 = float(input("Enter the first number: "))
    operation = str(input("Enter the operation : " ))
    num2 = float(input("Enter the second number: "))
    
    
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please try again.")

calculator()