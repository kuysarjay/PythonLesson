correct_username = "admin"
correct_password = "1234"

for attempt in range(3):
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect username or password.")

else:
    print("Account locked. Too many failed attempts.")