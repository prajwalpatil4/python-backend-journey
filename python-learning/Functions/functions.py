#A function in python is a block of code that runs only when it is called

#Created function for login credential
def my_function(username, password, ):
    print(f"Enter username: {username}")
    print(f"Enter Password:  {password},")
    print()

my_function("Prajwal11", 12345678)

#calling function many times
my_function("Prajwal11", 12345678)
my_function("Prajwal11", 12345678)
my_function("Prajwal11", 12345678)

"""
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
"""
def calculate_sum(sum):
    print(f"sum of two numbers: {sum}")
    print()

def _private_function(bank_account_number):
    print(f"Bank account number:  {bank_account_number}") 
    print()

def myFunction2(name):
    print(f"Hello, {name}")
    print()

calculate_sum(2+2)
_private_function(123456789)
myFunction2("Prajwal")