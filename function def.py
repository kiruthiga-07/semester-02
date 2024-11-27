#1
def withdraw(w):
    global balance
    balance-=w
    print("withdraw successfully, go back to the main balance.")
def deposit(d):
    global balance
    balance+=d
    print("deposited successfully")
def check_balance():
    print("your balance is :",balance)
def end_transaction():
    quit()
balance=20000
print("***KKK Bank***")
while True:
    print("1.Withdraw\n2.Deposit\n3.Balance\n4.Exit")
    option=int(input("Enter the transaction to proceed:"))
    match option:
        case 1:
            draw=int(input())
            withdraw(draw)
        case 2:
            dep=int(input())
            deposit(dep)
        case 3:
            check_balance()
        case 4:
            end_transaction()
        case _:
            print("Enter the valid option")



            
