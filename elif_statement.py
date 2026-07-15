# Elif statement in Python is used to check multiple conditions. 
# It stands for "else if" and allows you to test additional conditions if the previous ones were not true.
# Condition is from higher to lower, and the first condition that evaluates to TRUE will be executed,
    # and the rest will be skipped. 
# Here's an example of how to use elif statements:

#structure of an elif statement:
# if condition1:
    # block of code to be executed if condition1 is TRUE,
# elif condition2:
    # block of code to be executed if condition2 is TRUE,
# elif condition3:
    # block of code to be executed if condition3 is TRUE,
# else:
    # block of code to be executed if all conditions are FALSE.

# Example of an elif statement in Python:
grade = int(input("Enter your grade: "))  # Taking user input for grade and converting it to an integer.

if grade >= 90:
    print("You got an A.")  # This line will be executed because the condition is TRUE.
elif grade >= 80:
    print("You got a B.")  # This line will be executed because the condition is TRUE.
elif grade >= 70:
    print("You got a C.")  # This line will be executed because the condition is TRUE.
else:
    print("You failed the exam.")  # This line will be executed because all previous conditions are FALSE.