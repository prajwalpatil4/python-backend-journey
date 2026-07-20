"""Module is a file containing definitions and statements. 
A module can define functions, classes and variables. 
Modules help organize code into separate files so that programs become easier to maintain and reuse. 
Instead of writing everything in one place, related functionality can be grouped into its own module and imported whenever needed.
"""
#creating a Module
# calc.py
def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)

import calc
print(calc.add(10, 2))
print(calc.subtract(10, 2))

# This allows importing specific functions, classes, or variables rather than the whole module.
from math import sqrt, factorial
print(sqrt(16))
print(factorial(6)) 
#or

# * imports everything from a module into the current namespace.
from math import *
print(sqrt(16))
print(factorial(6))

#shorten a module's name using as.
import math as m
print(m.pi)

#built in random module.
import random
print(random.randint(1, 5))#will print any number between 1 and 5 range.

#module defined by user.
import calc
print(calc.subtract(20, 5))
