students={}
def add_student():
    student_id=input("Enter student ID:")
    if student_id in students:
        print("student ID already exists!")
        return
    name=input("Enter student name:")
    grade=input("Enter student grade:")
    major=input("Enter student major:")
    students[student_id]={"Name":name,"Grade":grade,"Major":major}
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
    else:
        for student_id, details in students.items():
            print(f"ID:{student_id},Name:{details['Name']},Grade:{details['Grade']},Major:{details['Major']}")

def remove_student():
    student_id=input("Enter student ID to remove:")
    if student_id in students:
        del students[student_id]
        print("student removed successfully!")
    else:
        print("student not found!")

def update_student():
    student_id=input("Enter student ID to update:")
    if student_id in students:
        name=input("Enter new student name:")
        grade=input("Enter new student grade:")
        major=input("Enter new student major:")

        if name:
            students[student_id]["Name"]=name
        if grade:
            students[student_id]["Grade"]=grade
        if major:
            students[student_id]["Major"]=major
        print("student details updated successfully!")
    else:
        print("student not found!")

def search_student():
    student_id=input("Enter student ID to search:")
    if student_id in students:
        details=students[student_id]
        print(f"ID:{student_id}, Name:{details['Name']},Grade:{details['Grade']},Major:{details['Major']}")
    else:
        print("student not found!")

def exit_program():
    print("Goodbye!")
    quit()

def main():
    while True:
        print("\nStudent Management Systems")
        print("1.Add student")
        print("2.Display student")
        print("3.Remove student")
        print("4.Update student")
        print("5.Search student")
        print("6.Exit")
        option=input("Enter your choice:")
        if option=="1":
            add_student()
        elif option=="2" :
            display_students()
        elif option=="3":
            remove_student()
        elif option=="4":
            update_student()
        elif option=="5":
            search_student()
        elif option=="6":
            exit_program()
        else:
            print("Invalid choice.please try again.")
main()                    
