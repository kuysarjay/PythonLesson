# Nested For Loop is a control flow statement that allows code to be executed repeatedly for a fixed number of iterations within another for loop.
# It is commonly used to iterate over multi-dimensional data structures (like lists of lists) or to perform actions that require multiple levels of iteration.
    # outer loop iterates over the outer sequence,
    # while the inner loop iterates over the inner sequence for each iteration of the outer loop.

# structure of a nested for loop:
# for outer_variable in outer_sequence:
#     for inner_variable in inner_sequence:
#         # Code to be executed for each combination of outer and inner variables

# Example of a nested for loop in Python:
for row in range(5):
    for col in range(5):
        print("*", end="  ")  # Print an asterisk with a space after it.
    print()  # Print a new line after each row is completed.