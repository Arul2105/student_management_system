
import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    student = {"roll": roll, "name": name, "dept": dept}
    students.append(student)
    save_students(students)
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No Students Found")
    for s in students:
        print(s)

def search_student():
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            print("Student Found:", s)
            return
    print("Student Not Found")

def delete_student():
    roll = input("Enter Roll Number: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("Student Deleted!")
            return
    print("Student Not Found")

students = load_students()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
