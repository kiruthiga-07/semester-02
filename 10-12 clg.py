"""
#1
class Department:
    def __init__(self,department):
        self.department=department
    def display_details(self):
        print(f"Department:{self.department}")
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_student(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class display_info(Department,Student):
    def __init__(self,department,name,age):
        Department.__init__(self,department)
        Student.__init__(self,name,age)
    def display_stu_info(self):
        self.display_details()
        self.display_student()

d=input("Enter the department:")
n=input("Enter the name:")
a=int(input("Enter the age:"))

s=display_info(d,n,a)
s.display_stu_info()
"""
#2 --hybrid
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nAge:{self.age}")
        
class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"ID:{self.eid}")
        
class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayManagerInfo()
        print(f"Department:{self.dept}")
        
class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamInfo(self):
        self.displayDeveloperInfo()
        print(f"Team Size:{self.teamsize}")
Name=input("Enter the name:")
Age=int(input("Enter the age:"))
EID=input("Enter the Employee ID:")
Dept=input("Enter the Department:")
TS=int(input("Enter the Team Size:"))
t=TeamLeader(Name,Age,EID,Dept,TS)
t.displayTeamInfo()

