"""
set = {} unordered collection of unique elements and is mutable,
    but we can add or remove elements from it.
"""

#set

my_favorite = {1, 2, 3, 4, "Stocks", "Forest", "Apple",}
print(my_favorite) #will print the set

#type() is a built-in function that returns the type of the object
print(type(my_favorite)) #will print type of the set

print(len(my_favorite)) #will print the length of the set
#.add() is a method that adds an element to the set
my_favorite.add("Samsung") #will add the element Samsung to the set
#.remove() is a method that removes an element from the set
my_favorite.remove(4) #will remove the element 4 from the set
print(my_favorite) #will print the updated set

empty_set = set()
print(type(empty_set))

#duplicate elements are not allowed in a set
my_favorite.add("Apple") #will not add the element Apple to the set because it already exists
print(my_favorite) #will print the updated set

#creating a set with duplicate elements
numbers = {1, 2, 2, 3, 3, 4} #2 and 3 are duplicate elements and will not be added to the set
print(numbers)

#membership testing in a set
print(1 in numbers) #will print True because 1 is in the set
print(5 in numbers) #will print False because 5 is not in the set
print("Stocks" in my_favorite) #will print True because Stocks is in the set
print("Samsung" not in numbers) #will print True because Samsung is not in the set

#operations on sets
A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B)) #will print the union of sets A and B
print(A.intersection(B)) #will print the intersection of sets A and B
print(A.difference(B)) #will print the difference of sets A and B
print(A ^ B) #will print the symmetric difference of sets A and B

#subset, superset, and disjoint operations
A.issubset(B)
A.issuperset(B)
A.isdisjoint(B)
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
"""
union() is a method that returns a new set with all the elements from both sets
intersection() is a method that returns a new set with only the elements that are common to both sets
difference() is a method that returns a new set with the elements that are in the first set but not in the second set
symmetric_difference() is a method that returns a new set with the elements that are in either set but not in both sets
refer 1st year puc science book for more operations on sets
"""

#immutable set = frozenset() is a built-in function that returns an immutable set object.
numbers = frozenset([1,2,3])

print(numbers)
numbers.add(4) #will raise an error because frozenset is immutable
