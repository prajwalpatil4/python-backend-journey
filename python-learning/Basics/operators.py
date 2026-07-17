"""Arithmetic operators are used to perform basic mathematical operations
    like addition, subtraction, multiplication and division.

In Python, the division operator (/) returns a floating-point result, 
    while floor division (//) returns an integer result.
"""
#arithmetic operators

a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

#Relational operators

"""
Comparison(or Relational) operators are used to compare two values and return a boolean result (True or False).
"""

a = 25
b = 24

print(a > b) # True
print(a < b) # False
print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a <= b) # False

#Logical operators

"""
Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

The precedence of Logical Operators in Python is as follows:

Logical not
logical and
logical or
"""

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Bitwise operators

"""
Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

Bitwise Operators in Python are as follows:

Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR
"""

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#Assignment Operators
"""Assignment operators are used to assign values to the variables. This operator 
is used to assign the value of the right side of the expression to the left side operand.
"""
a = 10
b = 5

b += a
print(b)

b -= a
print(b)

b *= a
print(b)

b //= 2
print(b)

b %= 3
print(b)

b **= 2
print(b)

#Identity Operators
""" 
"is" and "is not" are the identity operators and both are used to check if two values 
are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

is          True if the operands are identical 
is not      True if the operands are not identical 
"""
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

