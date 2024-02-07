def menu():
    print("\n\n**** MENU ****")
    print("1. Admit Student")
    print("2. Display Student List")
    print("3. Update Student Information")
    print("4. Search Student by ID")
    print("5. Calculate Average Age")
    print("6. Remove Student by ID")
    print("7. Exit")

def get_student_details():
    details = {}
    details['Student ID'] = int(input("Enter Student ID: "))
    details['Name'] = input("Enter Name: ")
    details['Age'] = int(input("Enter Age: "))
    details['Course'] = input("Enter Course: ")
    return details

def admit_student(students):
    student = get_student_details()
    students.append(student)

def display_student_list(students):
    for student in students:
        print("\nStudent ID: ", student['Student ID'])
        print("Name: ", student['Name'])
        print("Age: ", student['Age'])
        print("Course: ", student['Course'])

def update_student_info(students):
    id = int(input("Enter Student ID to update: "))
    index = next((index for index, student in enumerate(students) if student['Student ID'] == id), None)
    if index is None:
        print("Student not found")
    else:
        info = input("Enter information to update (Name, Age, or Course): ")
        students[index][info] = input("Enter new " + info + ": ")

def search_student_by_id(students):
    id = int(input("Enter Student ID to search: "))
    index = next((index for index, student in enumerate(students) if student['Student ID'] == id), None)
    if index is None:
        print("Student not found")
    else:
        student = students[index]
        print("\nStudent ID: ", student['Student ID'])
        print("Name: ", student['Name'])
        print("Age: ", student['Age'])
        print("Course: ", student['Course'])

# def calculate_average_age(students):
#     total_age = sum(student['Age'] for student in students)
#     average_age = total_age / len(students)
#     print("\nAverage Age: ", average_age)

def calculate_average_age(students):
    valid_ages = [int(student['Age']) for student in students if str(student['Age']).isdigit()]
    if valid_ages:
        total_age = sum(valid_ages)
        average_age = total_age / len(valid_ages)
        print("\nAverage Age: ", average_age)
    else:
        print("No valid ages to calculate average.")


def remove_student_by_id(students):
    id = int(input("Enter Student ID to remove: "))
    students[:] = [student for student in students if student['Student ID'] != id]

students = []

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        admit_student(students)
    elif choice == 2:
        display_student_list(students)
    elif choice == 3:
        update_student_info(students)
    elif choice == 4:
        search_student_by_id(students)
    elif choice == 5:
        calculate_average_age(students)
    elif choice == 6:
        remove_student_by_id(students)
    elif choice == 7:
        break
    else:
        print("Invalid choice")