# This is a simple Python program that takes user input and prints a greeting message.

"""
user_input.py is a Python script that demonstrates how to take 
user input using the input() function and print a greeting message using the print() function.

The script prompts the user to enter their name, and then it prints a personalized 
greeting message using the name provided by the user.
"""
#taking user input using the input() function

name = input("Enter your name: ")
print("Hello", name)

#taking user input for age and printing it

age = input("Enter your age: ")
print("You are", age, "years old.")

#converting the age input to an integer and calculating the year of birth.

age_str = int(age)
current_year = 2026
birth_year = current_year - age_str
print("You were born in", birth_year)

#converting input to float and calculating total price with tax.

"""
tax_rate = 0.05 
total = price * (1 + tax_rate)
so for example, if the user inputs a price of 100, the total with tax would be 105.0.
"""
price = float(input("Enter the item price: "))
tax_rate = 0.05
total = price * (1 + tax_rate)
print("Total with tax:", total)