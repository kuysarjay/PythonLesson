# The ternary operator is a shorthand way of writing an if-else statement in a single line.
# It allows you to assign a value to a variable based on a condition, making your code more concise.

# Structure of a ternary operator:
# variable = value_if_true if condition else value_if_false 

# Example of a ternary operator in Python:
age = int(input("Enter your age: "))  # Taking user input for age and converting it to an integer.
is_adult = True if age >= 18 else False
print(f"Is the person an adult? {is_adult}")