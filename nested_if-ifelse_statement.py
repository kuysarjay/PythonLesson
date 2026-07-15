# Nested If statements are a way to check multiple conditions by placing one if statement inside another. 
# This allows for more complex decision-making in your code.
    # Parent-nested if statements can be used to check for additional conditions only if the previous condition is TRUE.
    # Outside-inside nested if statements can be used to check for conditions that are independent of each other.
    # Outer-inner nested if statements can be used to check for conditions that are dependent on each other.
# Nested If-Else statements are similar to nested if statements,
    # but they also include an else clause that allows for 
    # alternative actions to be taken if the conditions are not met.

# Structure of a nested if statement:
# if condition1:
    # if condition2:
        # block of code to be executed if both condition1 and condition2 are TRUE.

# Example of a nested if statement in Python:
username = "admin"
password = "password"

input_username = input("Enter your username: ")  # Taking user input for username.
input_password = input("Enter your password: ")  # Taking user input for password.

if input_username == username:
    if input_password == password:
        print("Login successful.")  # This line will be executed because both conditions are TRUE.

# Structure of an nested if-else statement:
# if condition1:
    # if condition2:
        # block of code to be executed if both condition1 and condition2 are TRUE.
    # else:
        # block of code to be executed if condition1 is TRUE but condition2 is FALSE.
# else:
    # block of code to be executed if condition1 is FALSE.
    else:
        print("Incorrect password.")  # This line will be executed if the first condition is TRUE but the second condition is FALSE.
else:
    print("Incorrect username.")  # This line will be executed if the first condition is FALSE.        