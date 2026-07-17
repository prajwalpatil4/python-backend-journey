#Creating tuples
"""
The tuple data type is almost identical to the list data type, except in two ways.

First, tuples are typed with parentheses instead of square brackets. 
Second, the main benefit of using a tuple instead of a list is that it is immutable,
    meaning that once a tuple is created, it cannot be modified.
"""
companies = ("Google", "Microsoft", "Apple", "Amazon")
print(companies) #Output: ('Google', 'Microsoft', 'Apple', 'Amazon')

#Characteristics of tuples

"""
1. Tuples are ordered, meaning that the items have a defined order, and that order will not change.
2. Tuples are immutable, meaning that they cannot be changed after they are created.
3. Tuples allow duplicate values, meaning that two or more items can have the same value.
"""
#Indexing and slicing tuples

#indexing tuples
print(companies[0]) #Output: Google

#slicing tuples
print(companies[1:3]) #Output: ('Microsoft', 'Apple')


#Tuple Methods
# Tuple Methods
"""
Tuples have only two built-in methods:

1. count() - Returns the number of times a specified value occurs in the tuple.
2. index() - Returns the index of the first occurrence of the specified value.
"""

print(companies.count("Google")) #Output: 1
print(companies.index("Microsoft")) #Output: 1

#Packing and Unpacking
""" 
Packing is when we create a tuple by grouping multiple values together.
Unpacking is when we extract the values of a tuple into individual variables.

"""

student = ("Prajwal", 21, "CSE") # A tuple can store multiple data types.

name, age, branch = student

print(name)
print(age)
print(branch)