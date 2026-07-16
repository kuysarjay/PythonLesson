# Infinite Loop is a loop that never ends. It continues to execute the block of code indefinitely because the loop's condition always evaluates to true.
# Infinite loops can be created using a while loop with a condition that is always true, such as 'while True:'.
# Infinite Loops can be stopped by using a break statement, which allows you to exit the loop when a certain condition is met.

# Example of an infinite loop in Python:
while True:  # This condition is always true, creating an infinite loop.
    user_input = input("Enter 'exit' to stop the loop: ")  # Prompt the user for input.
    if user_input == 'exit':  # Check if the user input is 'exit'.
        print("Exiting the loop.")  # Inform the user that the loop will exit.
        break  # Exit the loop using the break statement.
    else:
        print(f"You entered: {user_input}")  # Print the user's input if it's not 'exit'.
