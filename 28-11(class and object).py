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
