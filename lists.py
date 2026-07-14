# Lists - is a variable type that can hold multiple values. 
# Lists are created using square brackets [] and can contain elements of different data types.
# Lists are ordered, fixed positional, and mutable (can be changed after creation).
# Lists are can be duplicated, meaning they can contain the same value multiple times.
    # indexing starts at 0, so the first element is at index 0, the second at index 1, and so on.
    # accessing elements in a list can be done using their index, 
        # e.g., my_list[0] will give you the first element.
    # modifying elements in a list can be done by assigning a new value to a specific index, 
        # e.g., my_list[0] = "new_value" will change the first element to "new_value".
    # adding elements to a list can be done using the append() method, 
        # e.g., my_list.append("new_element") will add "new_element" to the end of the list.
    # removing elements from a list can be done using the remove() method, 
        # e.g., my_list.remove("element_to_remove") will remove the first occurrence of "element_to_remove" from the list.

# Example of a list:
my_list = [1, 2, 3, "four", "five", 6.0, True]
print(my_list)

# Accessing elements in a list:
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: "four"

# Modifying elements in a list:
my_list[0] = "one"
print(my_list)  # Output: ["one", 2, 3, "four", "five", 6.0, True]

# Adding elements to a list:
my_list.append("seven")
print(my_list)  # Output: ["one", 2, 3, "four", "five", 6.0, True, "seven"]

# Removing elements from a list:
my_list.remove("four")
print(my_list)  # Output: ["one", 2, 3, "five", 6.0, True, "seven"]