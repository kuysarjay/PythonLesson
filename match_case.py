# Match case statement in Python 3.10 and later allows for pattern matching,
# which can be used to simplify complex conditional logic. 

# Here's an example of how to use a match case statement:
choice = input("Enter a fruit (apple, banana, cherry): ")  # Taking user input for fruit choice.
match choice:
    case "apple":
        print("You chose an apple.")  # This line will be executed if the user inputs "apple".
    case "banana":
        print("You chose a banana.")  # This line will be executed if the user inputs "banana".
    case "cherry":
        print("You chose a cherry.")  # This line will be executed if the user inputs "cherry".
    case _:
        print("Invalid choice.")  # This line will be executed if the user inputs anything other than "apple", "banana", or "cherry".
