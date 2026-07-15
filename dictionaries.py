# Dictionaries are collections of key-value pairs.
# Dictionaries are unordered, changeable, and do not allow duplicates.
# Dictionaries are written with curly brackets {} and have keys and values.
# Dictionaries can be accessed using their keys.
# Dictionaries can be modified by adding, changing, or removing key-value pairs.

# Example of a dictionary:
my_dict = {"name": "John",
           "age": 30,
           "city": "New York"
           }
print(my_dict)

# Accessing values in a dictionary:
print(my_dict["name"])  # Output: "John"
print(my_dict["age"])   # Output: 30

# Changing values in a dictionary:
my_dict["age"] = 31
print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York"}

# Adding new key-value pairs to a dictionary:
my_dict["occupation"] = "Engineer"
print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York", "occupation": "Engineer"}

# Removing key-value pairs from a dictionary:
del my_dict["city"]
print(my_dict)  # Output: {"name": "John", "age": 31, "occupation": "Engineer"}