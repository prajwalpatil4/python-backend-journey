# A simple if-else program to check the amount of money a person has
"""
This program prompts the user to enter their age and checks 
    if it is greater than 18. If the age is greater than 18, it prints "You are an adult."
    Otherwise, it prints "You are not an adult."
"""
a = int(input("Enter your age: "))
if a > 18:
    print("you are an adult.")
else:
    print("You are not an adult.")


# A simple if-else program to check if a person is allowed to enter a club based on their age and ID

age = int(input("Enter age: "))
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Bring your ID.")
else:
    print("You are underage.")