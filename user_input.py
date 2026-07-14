# User input using strings

# Using input() function to get user input
name = input("Enter your name: ")

#length - number of characters in the string
length = len(name)

#upper() - converts all characters in the string to uppercase
upper_name = name.upper()

#lower() - converts all characters in the string to lowercase
lower_name = name.lower()

print(f"Your name is {name}")
print(f"Length of your name: {length}")
print(f"Your name in uppercase: {upper_name}")
print(f"Your name in lowercase: {lower_name}")