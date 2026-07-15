# Match case using integers in Python 3.10 and later allows for pattern matching with numeric values.

# Here's an example of how to use a match case statement with integers:
number = int(input("Enter a number (1, 2, or 3): "))  # Taking user input for a number and converting it to an integer.
match number:
    case 1:
        print("You entered one.")  # This line will be executed if the user inputs 1.
    case 2:
        print("You entered two.")  # This line will be executed if the user inputs 2.
    case 3:
        print("You entered three.")  # This line will be executed if the user inputs 3.
    case _:
        print("Invalid number.")  # This line will be executed if the user inputs anything other than 1, 2, or 3.
