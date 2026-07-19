"""
In programming you often need to know if an expression is True or False.

we can evaluate any expression in Python, and get one of two answers, True or False.

"""
#comparing two values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Boolean based on condition
a = 12
b = 24

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#evaluating two variables x and y
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#printing boolean by calling a function.
def myFunction() :
  return True

print(myFunction())#functions can return true or false