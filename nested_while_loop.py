# Nested While Loop is a control flow statement that allows code to be executed repeatedly for a fixed number of iterations within another while loop.
# It is commonly used to iterate over multi-dimensional data structures (like lists of lists) or to perform actions that require multiple levels of iteration.
    # outer loop iterates over the outer sequence
    # while the inner loop iterates over the inner sequence for each iteration of the outer loop

# structure of a nested while loop:
# while outer_condition:
#     while inner_condition:
#         # Code to be executed for each combination of outer and inner conditions

# Example of a nested while loop in Python:
row = 0  # Initialize the outer counter to 0.
while row < 5:  # Start the outer while loop that will iterate 5
    col = 0  # Initialize the inner counter to 0.
    while col < 5:  # Start the inner while loop that will iterate 5
        print("*", end=" ")  # Print an asterisk with a space after it.
        col += 1  # Increment the inner counter by 1.
    print()  # Print a new line after each row is completed.
    row += 1  # Increment the outer counter by 1.