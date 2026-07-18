# List Comprehension

"""
List comprehension is a concise way to create lists in Python. 
    It allows you to generate a new list by applying an expression 
    to each item in an existing iterable (like a list, tuple, or range) 
    and optionally filtering the items based on a condition.
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

