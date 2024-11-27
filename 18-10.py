"""#single inheritance
class Student:#parent class
    def display(self):
        print("Base class-parent")
class Student_derived(Student):#inheritance applied----child class
    def show(self):
        print("Derived class-child")

s=Student_derived()#object creation
s.display()
s.show()

#multiple inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name={self.name}\nAge={self.age}")
class Student(person):
    def __init__(self,name,age,stu_id,stu_dept):
        super().__init__(name,age)
        self.stu_dept=stu_dept
        self.stu_id=stu_id
    def printDetails(self):
        self.display()
        print(f"ID={self.stu_id}\nDepartment={self.stu_dept}")
s=Student('kiruthiga',17,1200,'AI')
s.printDetails()"""


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(f"Employee Name={self.name}\nEmployee Salary={self.salary}")
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def Display_details(self):
        self.display_details()
        print(f"Department={self.department}")
s=Manager('kiruthiga',50000,'HR')
s.Display_details()
print()

class LibraryItem:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
    def displayinfo(self):
        print(f"Title={self.title}\nAuthor={self.author}\nPublication Year={self.publication_year}")
class Book(LibraryItem):
    def __init__(self,title,author,publication_year,genre):
        super().__init__(title,author,publication_year)
        self.genre=genre
    def Displayinfo(self):
        self.displayinfo()
        print(f"Genre={self.genre}")
s=Book('Harry Potter','J.K.Rowling',1997,'fantasy fiction')
s.Displayinfo()
print()

class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Amount Deposited:{amount}")
        else:
            print(f"Amount to deposit should be positive")
    def Withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds...")
        elif amount<0:
            print("Withdraw amount should be positive")
        else:
            self.balance-=amount
            print(f"Amount Withdraw:{amount}")
    def check_balance(self):
        print(f"Balance:{self.balance}")
my_account=BankAccount()
my_account.deposit(50000)
my_account.Withdraw(1000)
my_account.check_balance()
