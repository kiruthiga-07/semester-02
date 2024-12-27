#__(private)
#_(protected)
#normal(public)
"""class Student:                      #__(private)
    __id=123 #class variable
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)

s=Student("Ria")
s.display()
print(s.id)

class Student:                      #__(private)
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
a=input("Enter your Name: ")
s=Student(a)
s.display()


class Student:
    __id=int(input("Enter your ID: "))
    def __init__(self):
        self.__name=input("Enter your Name: ")
    def display(self):
        print("Name=",self.__name)
s=Student()
s.display()
print(s.id)

#
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
emp=Employee("kiruthiga",10000)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)

#
class Employee:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.__salary=int(input("Enter your salary: "))
emp=Employee()
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)

"""

class person:
    id=int(input("Enter ID:"))
    def __init__(self):
        self.__name=input("Enter name:")
        self.__age=int(input("Enter age:"))
class student(person):
    def __init__(self):
        self.stu_id=input("Enter student id:")
class Employee(person):
    def __init__(self):
        self.__emp_id=input("Enter Employee id:")

class Display_details(student,Employee,person):
    def __init__(self):
        person.__init__(self)
        student.__init__(self)
        Employee.__init__(self)

m=Display_details()
print(f"Name of the person: {m.person__name}\nAge of the person: {m._person_age}")
print(f"Student Id: {m.stu_id}")
print(f"Employee Id: {m.Employee_emp_id}")

