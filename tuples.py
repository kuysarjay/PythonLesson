# Tuples is a collection of items which is ordered and unchangeable.
# Tuples is ordered, allow duplicate and immutable.
# Tuples are written with round brackets.
# Tuples are created by placing all the items (elements) inside parentheses (), separated by commas.
# Tuples can contain any type of data, including numbers, strings, lists, and even other tuples.
# Tuples can be accessed using indexing, slicing, and iteration.

# Example of a tuple:
my_tuple = (1, 2, 3, "four", "five", 6.0, True)
print(my_tuple)

# Indexing in a tuple:
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: "four"

# Slicing in a tuple:
print(my_tuple[1:4])  # Output: (2, 3, "four")  
print(my_tuple[:3])  # Output: (1, 2, 3)

# Iterating through a tuple:
for element in my_tuple:
    print(element)  # Output: elements of the tuple in order

# Checking for membership in a tuple:
print("five" in my_tuple)  # Output: True
print("six" in my_tuple)  # Output: False