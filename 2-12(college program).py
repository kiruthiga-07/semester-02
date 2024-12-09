#1 multilevel inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)
class Employee(Person):
    def __init__(self,name,age,id):
        super(). __init__(name,age)
        self.id=id
    def displayEmployee(self):
        self.displayPerson()
        print("ID=",self.id)
class Manager(Employee):
    def __init__(self,name,age,id,salary):
        super(). __init__(name,age,id)
        self.salary=salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary=",self.salary)
man=Manager("kiruthiga",17,100,29000)
man.displayManager()

#2 hierarchical
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        
class Developer(Employee):
    def __init__(self, name, emp_id,age):
        super().__init__(name, emp_id)
        self.age = age

    def display_details(self):
        super().display_details()
        print(f"age: {self.age}")
manager = Manager("kiruthiga", "M123", "HR")
manager.display_details()  
devel = Developer("hema", "D456", 30)
devel.display_details()
