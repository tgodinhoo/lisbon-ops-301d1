#!/usr/bin/python3

# Assign a list of ten string elements to a variable
my_list = ["apple", "banana", "beer", "corn", "strawberry", "wine", "beer", "snacks", "orange", "lemon"]

# Print the fourth element of the list (index 3 since indexing is 0-based)
print("Fourth element:", my_list[3])

# Print the sixth through tenth elements of the list (indices 5 to 9)
print("Sixth to tenth elements:", my_list[5:10])

# Change the value of the seventh element (index 6) to "onion"
my_list[6] = "onion"

# Print the updated list
print("Updated list:", my_list)

# Append an element to the list
my_list.append("mango")

# Create a copy of the original list
my_list_copy = my_list.copy()

# Count the number of times "beer" appears
count = my_list.count("beer")

# Extend the list with another list
my_list_copy.extend(["carrot", "pear"])

# Find the index of "beer" in the list
index = my_list.index("beer")

# Insert "peach" at a specific position (index 2)
my_list_copy.insert(2, "peach")

# Remove and return the last element of the list
popped_element = my_list_copy.pop()

# Remove the first occurrence of "banana" from the list
my_list_copy.remove("banana")

# Reverse the list
my_list_copy.reverse()

# Sort the list in alphabetical order
my_list_copy.sort()

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Create a set
my_set = {6, 7, 8, 9, 10}

# Create a dictionary
my_dict = {'FirstName': 'John', 'LastName': 'Smith', 'Age': '32'}

# Print the modified list, popped element, tuple, set and dictionary
print("Modified list: ", my_list_copy)
print("Popped element: ", popped_element)
print("Tuple: ", my_tuple)
print("Set: ", my_set)
print("Dictionary: ", my_dict)

# Clear the list
my_list.clear()