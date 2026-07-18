import os

balance = 1000

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=== BANKING SYSTEM ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"\nYour balance is: ${balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: $"))
        balance += amount
        print("Deposit successful!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: $"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")

    input("\nPress Enter to continue...")
