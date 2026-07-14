# Concatenation - combining strings together

# + method
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# join method
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)

# string formatting method
name = "Alice"
age = 30
info = f"My name is {name} and I am {age} years old."
print(info)

# old string formatting method
    # %d for integers
    # %s for strings
    # %f for floating-point numbers
    # %x for hexadecimal numbers
    # %c for single characters
    # %o for octal numbers
name = "Bob"
age = 25 
info = "My name is %s and I am %d years old." % (name, age)
print(info)


# format method
name = "Charlie"
age = 35
info = "My name is {} and I am {} years old.".format(name, age)
print(info)

# * method
word = "Hello"
repeated_word = word * 3
print(repeated_word)
