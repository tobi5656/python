print("This is a simple command line calculator.")
print("You can perform basic operations like addition, subtraction, multiplication, and division.\nPlease enter two numbers and the operation you want to perform.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")
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
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")
print("Thank you for using the command line calculator!")