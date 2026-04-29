# Student Profile Manager

students = [] # List to store student profiles

def add_student(): # Function to add a new student profile
    print("\n--- Add Student ---") #Prints the header 'Add Student' to indicate the start of the student addition process.
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")

    student = [name, age, city]
    students.append(student) #append means to put this item inside the list

    print("✅ Student added successfully!\n")


def view_students(): # Function to view all student profiles
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.\n") #the \n means new line. so it prints that no students are found, then it moves the cursour to a new line.
    else:
        for i, student in enumerate(students, start=1):
            name, age, city = student
            print(f"{i}. Name: {name} | Age: {age} | City: {city}")
        print()
"""This section means that it will go through the students list one by one ..... then 
it will give each student a number starting from 1 (because of start=1) and then it
will print the name, age, and city of each student in a formatted way. 
After it finishes printing all students, it will print a new line for better readability."""

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