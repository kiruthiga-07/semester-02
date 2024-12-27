#
import re
def validate_phone_number(phone):
    pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    if re.match(pattern,phone):
        return "Valid phone number"
    else:
        return "phone number is not valid"
phone=input()
print(validate_phone_number(phone))


#
class Student:
    def __init__(self):
        self.name=input("Enter your name:")
        self.mark=float(input("Enter your mark:"))
        self.grade=self.calculate_grade()
        if not self.name:
            raise ValueError("name should not be empty")
        if not self.name.isalpha():
            raise ValueError("Name must contain alphabet")
        if self.mark>100:
            raise ValueError("mark should be between 0-100")
    def calculate_grade(self):
        if self.mark>=90:
            return "Grade A"
        elif self.mark>=80:
            return "Grade B"
        elif self.mark>=70:
            return "Grade C"
        elif self.mark>=60:
            return "Grade D"
        else:
            return "Grade F"
    def  display(self):
        print(f"Name:{self.name}\nMark:{self.mark}\nGrade:{self.grade}")
try:
    s=Student()
    s.display()
except ValueError as e:
    print(e)
