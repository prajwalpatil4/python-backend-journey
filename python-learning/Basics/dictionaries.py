"""
Dictionaries in Python 
"""
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

data = { "name": "Prajwal", "age": 22 }
print(data)

#Creating a Dictionary
"""A dictionary is created by writing key-value pairs inside { }, 
    where each key is connected to a value using colon (:). 
    A dictionary can also be created using dict() function.
"""

student = { "name": "Prajwal", "age": 22, "courses": ["Math", "CompSci"] }
print(student)

#Accessing Dictionary Items
"""
A value in a dictionary is accessed by using its key. 
    This can be done either with square brackets [] or with the get() method. 
    Both return the value linked to the given key.
"""
print(student["name"])  # Accessing value using square brackets
print(student.get("courses"))  # Accessing value using get() method

#Adding and Updating Dictionary Items
"""
New items are added to a dictionary using the assignment operator (=) by giving a new key a value. 
If an existing key is used with the assignment operator, its value is updated with the new one.
"""
student["email"] = "prajwlpatil.research@gmail.com"

#len() function returns the number of items in a dictionary.
print(len(student))  # Output: 4

#Data Types of Dictionary Values
"""
Dictionary values can be of any data type, including strings, numbers, lists, or even other dictionaries.
"""
student = {
    "name": "Prajwal",
    "Robot": False,
    "age": 22,
    "courses": ["Math", "CompSci"],
    "address": {"city": "Pune", "state": "Maharashtra"}
}
print(type(student))

"""
The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary."""
student = dict(name="Prajwal", age=22, courses=["Math", "CompSci"]) #Using the dict() method to make a dictionary
print(student)

"""
difference between get() and [] for accessing dictionary items
    The get() method returns None if the key does not exist, 
    while using square brackets [] raises a KeyError.
"""
print(student.get("phone"))      # None
# print(student["phone"])        # Raises KeyError