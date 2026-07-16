# What exactly is a list in Python?
'''
List is a built-in data type in Python.

A list is:
1. Ordered – Items have a fixed position (index).
2. Changeable (Mutable) – Items can be added, removed, or modified.
3. Allows duplicate values.

A list is one of Python's four main collection data types:
1. List
2. Tuple
3. Set
4. Dictionary
'''

# How to create a list in Python?
print("\nCreating a list in Python")

"""
Here, 'fruit' is a variable that stores a single string value.

If we want to store multiple values in a single variable,
we can use a list.

Lists are created using square brackets [].
"""

fruit =  "apple"
print(fruit) # This will print the value of the variable 'fruit', which is "apple".

fruits = ["apple", "banana", "cherry", "date"]

print(fruits) # This will print the entire list of fruits.
print(type(fruits)) # This will print the type of the variable 'fruits', which is <class 'list'>.

# Accessing List Items
print("\nAccessing List Items")

print(fruits[0])     # apple
print(fruits[1])     # banana
print(fruits[-1])    # cherry

# Modifying List Items
print("\nModifying List Items")

fruits[1] = "orange"

print(fruits)

# Getting the Length of a List
print("\nGetting the Length of a List")

print(len(fruits)) # will print the number of items in the list 'fruits', which is 4.

#Append method
print("\nAppending an Item to a List")
'''
appending an item to the end of the list using the append() method. 
will add "mango" to the end of the list 'fruits'.
append() is used to add a string.
'''
fruits.append("mango")

print(fruits)

# Inserting Items into a List
print("\nInserting an Item into a List")
'''
inserting an item at a specific index in the list using the insert() method.
will insert "grapes" at index 1 in the list 'fruits'. but will not remove any existing items.
'''
fruits.insert(1, "grapes")

print(fruits)

# Removing Items from a List
print("\nRemoving an Item from a List")

'''
removing an item from the list using the remove() method. 
will remove the first occurrence of "banana" from the list 'fruits.'''

fruits.remove("orange")
fruits.pop()
del fruits[0]
print(fruits)

# Slicing a List
print("\nSlicing a List")

"""
Slicing a list means getting a subset of the list by specifying a range of indices. 
syntax for slicing a list is: list[start:end],
where 'start' is the index of the first item to include,
and 'end' is the index of the first item to exclude.
"""

numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

