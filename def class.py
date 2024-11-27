
#1
class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited {amount}.New balance is {self.balance}")
        else:
            print("Amount to deposit should be greater than 0.")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"withdrew {amount}.New balance is {self.balance}")
        elif amount>self.balance:
            print("Insufficient balance!")
        else:
            print("Amount to withdraw should be greater than 0")
    def check_balance(self):
        print(f"Account balance for {self.account_holder}:{self.balance}")
account=BankAccount("kiruthiga","123456789",1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
print()

#2
class Cosmetics:
    def __init__(self,name="Foundation",brand="Lakme",price=300,category="Makeup"):
        self.name=name
        self.brand=brand
        self.price=price
        self.category=category
    def display(self):
        print(f"Product name:{self.name}\nBrand:{self.brand}\nPrice:{self.price}\nCategory:{self.category}")
product=Cosmetics()
product.display()
        
