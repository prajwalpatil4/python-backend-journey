"""
array_basics.py

This program demonstrates basic array (list) operations in Python:
1. Creating an array
2. Accessing elements
3. Updating elements
4. Adding elements
5. Removing elements
6. Traversing the array
"""

# Create an array (list)
numbers = [10, 20, 30, 40, 50]

print("Original array:", numbers)

# Access elements
print("First element:", numbers[0]) #will print 10 
print("Last element:", numbers[-1])

# Update an element
numbers[2] = 35
print("After updating third element:", numbers)

# Add elements
numbers.append(60)
print("After appending 60:", numbers)

numbers.insert(1, 15)
print("After inserting 15 at index 1:", numbers)

# Remove elements
numbers.remove(40)
print("After removing 40:", numbers)

removed = numbers.pop()
print("Popped element:", removed)
print("Array after pop:", numbers)

# Traverse the array
print("\nTraversing the array:")
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")