# Break and Continue Statement is used to control the flow of loops in Python.
# The `break` statement is used to exit a loop prematurely,
    # while the `continue` statement is used to skip the current iteration and move to the next iteration of the loop.

# Example of break and continue statements in Python:
number = 0  # Initialize the number variable.
while number < 10:  # Loop through numbers from 0 to 9.
    if number == 7:  # Check if the current number is 7.
        print("Breaking the loop at number 7.")  # Inform the user that the loop will break.
        break  # Exit the loop when number is 7.
    elif number == 3:  # Check if the current number is 3.
        print("Skipping number 3.")  # Inform the user that number 3 will be skipped.
        number += 1  # Increment the number variable to avoid an infinite loop.
        continue  # Skip the current iteration when number is 3.
    else:
        print(f"Current number is: {number}")  # Print the current number if it's not 7.
    number += 1  # Increment the number variable.