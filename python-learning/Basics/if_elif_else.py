# A simple if-elif-else program to check the amount of money a person has
"""
if-elif-else statement is used to check the amount of money a person has and print a message accordingly.
if the amount is greater than 0, it prints "You have money."
if the amount is less than 0, it prints "You are in debt."
if the amount is equal to 0, it prints "You have no money."
"""
a = int(input("Enter how much money you have: "))

if a > 0:
    print("You have money.")
elif a < 0:
    print("You are in debt.")
else:
    print("You have no money.")
