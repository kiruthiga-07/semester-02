#multiple inheritance
class Employee:
    def __init__(self,name,ID,position):
        self.name=name
        self.ID=ID
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nID:{self.ID}\nPosition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print(f"Street:{self.street}\nState:{self.state}\nCountry:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,ID,position,street,state,country):
        super().__init__(name,ID,position)
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddressInfo()
ed=EmployeeDetails("Kiruthiga",21,"Manager","shenoy Nagar","Tamil nadu","India")
ed.displayEmp()

#multilevel inheritance
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

#hybrid inheritace
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_info(self):
        print(f"Name of the person: {self.name}\nAge of the person: {self.age}")
class student(person):
    def __init__(self,stu_id):
        self.stu_id=stu_id
    def student_info(self):
        print(f"Student Id: {self.stu_id}")
class Employee(person):
    def __init__(self,emp_id):
        self.emp_id=emp_id
    def Employee_info(self):
        print(f"Employee Id: {self.emp_id}")
class display_details(student,Employee,person):
    def __init__(self,name,age,stu_id,emp_id):
        person.__init__(self,name,age)
        student.__init__(self,stu_id)
        Employee.__init__(self,emp_id)
    def display_all(self):
        self.person_info()
        self.student_info()
        self.Employee_info()
m=display_details("Kiruthiga",17,"E24AI021",207645)
m.display_all()

#parametarised
class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}")

s=Library("Harry Potter","J.K.Rowling")
s.show()

#non-parametarised
class Library:
    def __init__(self):
        self.book="Harry potter"
        self.author="J.K.Rowling"

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}")

s=Library()
s.show()

#para and non-para mixed
class Library:
    def __init__(self,book,author="J.K.Rowling",published=1997):
        self.book=book
        self.author=author
        self.published=published

    def show(self):
        print(f"Book:{self.book}\nAuthor:{self.author}\nPublished:{self.published}")

s=Library("Harry Potter")
s.show()



#1-inheritance
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter ID:")
        self.name=input("Enter the name:")
        self.salary=int(input("Enter the salary:"))
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name,"\nSalary=",self.salary)
    def getSalary(self):
        return self.salary
class Perks(Employee):
    def calculateSalary(self):
        self.getEmployeeInfo()
        sal=self.getSalary()
        self.hra=sal*15/100
        self.da=sal*14/100
        self.total=self.hra+self.da
    def displayPerks(self):
        self.displayEmployeeInfo()
        print("Perks=",self.getSalary()+self.total)
p=Perks()
p.calculateSalary()
p.displayPerks()

#2
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary=",self.sal)

p=Perks()
p.getDetails()
p.displayInfo()

#3
class Inventory:
    def __init__(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print(f"Product ID:{self.prodId}\nProduct Name:{self.prodName}\nProduct Count:{self.prodCount}")
s=Inventory(123,"foundation",5)
s.display()

#4

class Inventory:
    def __init__(self):
        self.prodId=123
        self.prodName="Foundtion"
        self.prodCount=5
class display(Inventory):
    def dis(self):
        print(f"Product ID:{self.prodId}\nProduct Name:{self.prodName}\nProduct Count:{self.prodCount}")
product=display()
product.dis()
