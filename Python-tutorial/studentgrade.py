# Student Grade Manager using Dictionary

students = {}   # Empty dictionary

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print All Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add new student
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"Added: {name} - {grade}")

    # Update existing student
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            new_grade = input("Enter new grade: ")
            students[name] = new_grade
            print(f"Updated: {name} - {new_grade}")
        else:
            print("Student not found!")

    # Print all students
    elif choice == "3":
        if len(students) == 0:
            print("No students added yet.")
        else:
            print("\n--- Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")

    # Exit program
    elif choice == "4":
        print("Exiting program...")
        break

    # Invalid input
    else:
        print("Invalid choice! Please select 1-4.")
