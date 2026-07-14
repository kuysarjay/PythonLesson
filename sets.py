# Sets are unordered collections of unique elements. 
# They are useful for storing data that should not contain duplicates and for performing mathematical 
    # set operations like union, intersection, and difference.
# Sets are mutable, meaning you can add or remove elements after creation, 
    # but the elements themselves must be immutable (e.g., numbers, strings, tuples).
# Sets are created using curly braces {} or the set() function.
    # adding elements to a set can be done using the add() method, 
        # e.g., my_set.add("new_element") will add "new_element" to the set.
    # removing elements from a set can be done using the remove() method, 
        # e.g., my_set.remove("element_to_remove") will remove "element_to_remove" from the set.
    # accessing elements in a set is not done by index, since sets are unordered. 
        # Instead, you can iterate through the set or check for membership using the in keyword.
    # checking for membership in a set can be done using the in keyword, 
        # e.g., "element" in my_set will return True if "element" is in the set, otherwise False.

# Example of a set:
my_set = {1, 2, 3, "four", "five", 6.0, True}
print(my_set)

# Adding elements to a set:
my_set.add("six")
print(my_set)  # Output: {1, 2, 3, "four", "five", 6.0, True, "six"}

# Removing elements from a set:
my_set.remove("four")
print(my_set)  # Output: {1, 2, 3, "five", 6.0, True, "six"}

# Accessing elements in a set:
for element in my_set:
    print(element)  # Output: elements of the set in no particular order

# Checking for membership in a set:
print("five" in my_set)  # Output: True
print("four" in my_set)  # Output: False
