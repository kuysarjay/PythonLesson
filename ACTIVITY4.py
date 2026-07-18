print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

grade1 = float(input("Enter Grade in Math: "))
grade2 = float(input("Enter Grade in Science: "))
grade3 = float(input("Enter Grade in English: "))
grade4 = float(input("Enter Grade in History: "))

average = (grade1 + grade2 + grade3 + grade4) / 4

print("\nStudent Name:", name)
print("Average Grade:", round(average, 2))

if average >= 90:
    print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 70:
    print("Letter Grade: C")
elif average >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")