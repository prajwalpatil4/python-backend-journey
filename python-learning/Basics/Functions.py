"""
Functions in Python

A function is a block of code that runs only when it is called.

Functions can:
1. Perform a specific task.
2. Return a value.
3. Help avoid writing the same code repeatedly (code reusability).

Example:
Imagine you need to convert temperatures from Fahrenheit to Celsius
many times in your program. Instead of writing the same calculation
again and again, you can write a function once and call it whenever
needed.
"""

# Function definition
def say_hello(name):
    """Displays a greeting message."""
    print(f"Hello, {name}")
    print()


# Function calls
say_hello("Prajwal")
say_hello("Prajwal")
say_hello("Prajwal")

"""
We can call a function as many times as we want.

Example:
say_hello("john")
say_hello("Bob")
say_hello("Charlie")
"""


# Invoice Function
def display_invoice(username, amount, due_date):
    """Displays an invoice."""
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}.")


# Function call
display_invoice("Prajwal", 50, "11/11/2026")