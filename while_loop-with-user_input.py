# While Loop with User Input is a control flow statement that allows code to be executed repeatedly based on user input.
# The while loop can be thought of as a repeating if statement that continues until a certain condition is met, which in this case is determined by the user's input.

# Example of a while loop with user input in Python:
password = "admin"  # Set a predefined password.

while True:  # Start an infinite loop that will continue until the user enters the correct password.
    user_input = input("Please enter the password: ")  # Prompt the user to enter the password.
    
    if user_input == password:  # Check if the user's input matches the predefined password.
        print("Access granted!")  # Inform the user that access is granted.
        break  # Exit the loop since the correct password was entered.
    else:
        print("Access denied. Please try again.")  # Inform the user that access is denied and prompt to try again.