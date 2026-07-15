# Match case grouping allows for grouping multiple cases together, 
    # which can help reduce redundancy in your code.
    # it is a case sensitive statement, meaning that the input must match the case exactly as specified in the cases.

# Here's an example of how to use match case grouping:
day = input("Enter a day of the week: ")  # Taking user input for a day of the week.
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday.")  # This line will be executed if the user inputs any of the weekdays.
    case "Saturday" | "Sunday":
        print("It's a weekend.")  # This line will be executed if the user inputs either "Saturday" or "Sunday".
    case _:
        print("Invalid day.")  # This line will be executed if the user inputs anything other than the specified days of the week. 
