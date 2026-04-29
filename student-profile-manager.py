# Student Profile Manager



    student = [name, age, city]

    print("✅ Student added successfully!\n")


def view_students(): # Function to view all student profiles
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.\n")
    else:
        for i, student in enumerate(students, start=1):
            name, age, city = student
            print(f"{i}. {name} | Age: {age} | City: {city}")
        print()


def main():
    while True:
        print("====== Student Manager ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.\n")


# Run program
main()