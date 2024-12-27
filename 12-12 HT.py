class Student:
    def __init__(self,stu_id,name,grade):
        self.stu_id=stu_id
        self.name=name
        self.grade=grade
    def Validatedetails(self):
        if not (self.stu_id.startswith("STU") and self.stu_id[3:].isdigit() and len(self.stu_id)==7):
            return "Invalid student ID format.It should be in the format STU1234."
        if not (len(self.name)>=2 and all(char.isalpha() or char.isspace() for char in self.name)):
            return "Invalid name. It should be at least 2 characters long and contain only alphabet and spaces."
        valid_grade=[f"{i}th Grade" for i in range(1,13)]
        if self.grade not in valid_grade:
            return "Invalid grade. It should be in the format '<number>th Grade'(e.g., '1st Grade' to '12th Grade')."
        return "All details are valid."
    def display(self):
        print(f"Student ID:{self.stu_id}\nName:{self.name}\nGrade:{self.grade}")

stu_id=input("Enter the student ID: ")
name=input("Enter Name: ")
grade=input("Enter grade: ")

stu=Student(stu_id,name,grade)
validation_message=stu.Validatedetails()
print(validation_message)
if validation_message=="All details are valid.":
        stu.display()
