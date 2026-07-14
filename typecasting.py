# Type Casting in Python

# int() - converts a value to an integer
x = int(3.5)  # x = 3
y = int("10")  # y = 10
print(f"x: {x}, y: {y}")

# float() - converts a value to a floating-point number
x = float(5)  # x = 5.0
y = float("3.14")  # y = 3.14
print(f"x: {x}, y: {y}")

# str() - converts a value to a string
x = str(5)  # x = "5"
y = str(3.14)  # y = "3.14"
print(f"x: {x}, y: {y}")


birthyear = input("Enter your birth year: ")
age = 2026 - int(birthyear)
print(f"You are {age} years old.")