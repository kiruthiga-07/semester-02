"""#1
class User:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password

    def set_password(self):
        if len(self.__password)<8:
            return "Password must be 8 characters long."
        if not any(char.isdigit() for char in self.__password):
            return "Password must contain atleast one digit."
        if not any(char in "!@#$%^&*()_+?" for char in self.__password):
            return "Password must conatain atleast one special character."
        return "Password is valid."
        
    def check_password(self,input_password):
        return self.__password==input_password

username=input("Enter username: ")
password=input("Enter password: ")

user=User(username,password)

password_validation=user.set_password()
if password_validation=="Password is valid.":
    input_password=input("Re-enter password to check: ")
    if user.check_password(input_password):
        print("Password is valid.")
    else:
        print("Password is not valid.")
        
else:
    print(password_validation)
print()

#2
class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.set_price(price)
        self.set_stock(stock)
    def set_price(self,price):
        if price>0:
            self.__price=price
        else:
            print("Invalid price... Price must be greater than 0")
    def set_stock(self,stock):
        if type(stock) == int and stock >= 0:
            self.__stock=stock
        else:
            print("Invalid stock... Stock must be a non negative integer")
    def get_stock(self):
        return self.__stock
name=input("Enter the product name: ")
price=int(input("Enter the price: "))
stock=int(input("Enter the stock details: "))
prod=Product(name,price,stock)
prod.set_price(int(input("Re-enter price to check: ")))
prod.set_stock(int(input("Re-enter stock to check: ")))
print(f"Current Stock: {prod.get_stock()}")
print()

#3
class Student:
    def __init__(self,name,age,marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks

    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        if 5<= age <=100:
            self.__age=age
        else:
            print("Invalid age... Age must be between 5 and 100")
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self.__marks=marks
        else:
            print("Invalid marks... Marks must be between 0 and 100")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
mark=int(input("Enter your mark: "))
stu=Student(name,age,mark)
print(f"Name:{stu.get_name()}\nAge:{stu.get_age()}\nMarks:{stu.get_marks()}")
"""
a=0.98
print(a,type(a))
        
