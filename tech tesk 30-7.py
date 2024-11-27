#registration process
try:
    age=int(input("Enter the age:"))
    assert age>=18,"participant must be atleast 18 years old"
    assert age<=60,"participant must be no older than 60 years old"
    print("participant is eligible for registration.")
except AssertionError as e:
    print("Registration error:",e)

#calculator    
try:
    n1=int(input())
    n2=int(input())
    n3=n1+n2
    print(n3)
except TypeError as t:
    print(t)

#bank application
class NegativeWithdrawalError(Exception):
    pass
class InsufficientFundError(Exception):
    pass
try:
    balance=int(input("Enter the balance amount:"))
    amount=int(input("Enter amount to withdraw:"))
    if amount<0:
        raise NegativeWithdrawalError("Withdrawal amount cannot be negative")
    elif amount>balance:
        raise InsufficientFundError("Insufficient funds in your account")
    else:
        new_balance=balance-amount
        print(f"Withdrawn succesfully.Your new balance is {new_balance}")
        
except NegativeWithdrawalError as a:
    print(f"Error: {a}")
except InsufficientFundError as b:
    print(f"Error: {b}")

    
