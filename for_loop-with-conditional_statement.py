# For Loop with Conditional Statement is a control flow statement that allows code to be executed repeatedly for a fixed number of iterations, with the ability to include conditional logic within the loop. It is commonly used to iterate over a sequence (like a list, tuple, or string) and perform actions based on specific conditions.
# For Loop with Conditional Statement can be thought of as a repeating block of code that executes for each item in a sequence, with the option to include conditional statements that determine whether certain actions should be performed during each iteration.
# For Loop with Conditional Statement is determined by the number of items in the sequence or the range specified, and it continues until all items have been processed or the range is exhausted
    # range(start, stop, step) is a built-in function that generates a sequence of numbers. It can be used in a for loop to specify the number of iterations, and conditional statements can be used to control the flow of execution within the loop based on specific conditions.

# Example of a for loop with conditional statement in Python:
for i in range(1, 11):  # Start a for loop that will iterate 10 times (from 1 to 10).
    if i % 2 == 0:  # Check if the current number is even.
        print(f"{i} is even")  # Print that the number is even.
    else:  # If the number is not even, it must be odd.
        print(f"{i} is odd")  # Print that the number is odd.