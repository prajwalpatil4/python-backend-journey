# Loops is a programming construct that allows you to repeat a block of code multiple times. 
# In Python, there are two main types of loops: for loops and while loops.

# 1. For Loop:
""" A for loop is used to iterate over a sequence (like a range, list, tuple, or string) or other iterable objects. 
 It executes a block of code for each item in the sequence for fixed number of times.
"""
print("\nprinting numbers using for loop:")
for x in range(1,6):
    print(x, end="")  # This will print numbers from 1 to 5
                      #inside print if we write , end="" it will print numbers or strings in one line 
print("printing even numbers: ")
#printing even numbers from 1 to 10
for x in range(2,11,2):
    print(x, end="")  # This will print even numbers from 2 to 10
              #same way we can print odd numbers from 1 to 10

print("\nprinting reversed ordered numbers:")
#for loop but reverse order
for x in reversed(range(1,6)):
    print(x, end="")  # This will print numbers from 5 to 1
    #or
for x in range(5,0,-1):
    print(x, end="")  # This will also print numbers from 5 to 1

print("\nPrinting numbers from 1 to 9, except 6 (using continue):")
#continue key word
for x in range(1, 10):
    if x == 6:
        continue #will ignore 13
    else:
       print(x, end="")

print("\nprinting numbers with break key word: ")
for x in range(1, 10):
    if x == 6:
        break #will stop at 5 and does not continue printing
    else:
       print(x, end="")

print("\nPrinting for loops with strings: ")
#for loop with strings
for char in "Hello, World!":
    print(char, end="")

print("\nprinting iteration over strings: ")
#iterating over a string using for loop
price = "10000"

for x in price:
    print(x, end="")

# 2. While Loop:
""" A while loop is used to repeat a block of code as long as a condition is true.
"""
#print x as x is less than 5
x = 0
while x < 5:
    print(x)  # This will print numbers from 0 to 4
    x += 1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue and skip the current iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Taking input name and printing it with greeting
name = input("Enter your name: ")

while name == "name": 
    print("Hello" +(name))
print(f"Hello {name}")