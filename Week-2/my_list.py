# Create an empty list called my_list.
my_list = []
print(f"Initial empty list: {my_list}")

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.extend([10, 20, 30, 40])
print(f"List after appending elements: {my_list}")

# Insert the value 15 at the second position in the list.
my_list[1] = 15
print(f"Added 15 at second index: {my_list}")

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(f"Extended list with [50, 60, 70]: {my_list}")

# Remove the last element from my_list.
my_list.pop()
print(f"Removed last element: {my_list}")

# Sort my_list in ascending order.
my_list.sort()
print(f"Sorted list (Asc): {my_list}")

# Find and print the index of the value 30 in my_list.
print(f"Index of the element 30: {my_list.index(30)}")
