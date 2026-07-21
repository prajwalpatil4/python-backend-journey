"""
Python Calculator

This program performs basic arithmetic operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

The user enters an operator and two numbers.
The program calculates and displays the result.
"""

# Ask the user to enter the arithmetic operator
operator = input("Enter an operator (+ - * /): ")

# Get the first number from the user and convert it to a float
num1 = float(input("Enter the 1st number: "))

# Get the second number from the user and convert it to a float
num2 = float(input("Enter the 2nd number: "))

# Check if the user selected addition
if operator == "+":
    result = num1 + num2
    print(round(result, 3))   # Display the result rounded to 3 decimal places

# Check if the user selected subtraction
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

# Check if the user selected multiplication
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

# Check if the user selected division
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

# Execute if the operator entered is invalid
else:
    print(f"The '{operator}' is not a valid operator.")
