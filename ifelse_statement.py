# If else statement is a conditional statement that allows you to execute one block of code
    # if a specified condition is TRUE, and another block of code if the condition is FALSE.
# It is commonly used in programming to control the flow of execution based on certain criteria.

# Structure of an if else statement:
# if condition:
    # block of code to be executed if the condition is TRUE,
# else:
    # block of code to be executed if the condition is FALSE.


# Example of an if else statement in Python:
grade = int(input("Enter your grade: ")) # Taking user input for grade and converting it to an integer.

if grade >= 75:
    print("You passed the exam.")  # This line will be executed because the condition is TRUE.
else:
    print("You failed the exam.")  # This line will be executed because the condition is FALSE.