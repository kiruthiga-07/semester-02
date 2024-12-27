#1 You are building a program to track user login attempts
loginid="KIRU3768"
max_attempts=5
attempts=0

while attempts<max_attempts:
    user_login=input("Enter your login id: ")
    if user_login==loginid:
        print("Login successful")
        break
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts
        print(f"Incorrect login. you have {remaining_attempts} attempts remaining")

        if attempts==max_attempts:
            print("Account is locked due to too many failed attempts")

#2) Remove duplicates. Sort the list in descending order.
n=[6,8,4,5,3,8,6]
r=list(set(n))
print(r)
s=sorted(n,reverse=True)
print(s)

#
n=(list(map(int,input('Enter the elements: ').split())))
r=list(set(n))
print(r)
s=sorted(n,reverse=True)
print(s)

#3) Write a program that takes a number as input and returns the sum of its digits.
number=input("Enter the number:")
s=0 
for digit in number:
    s+=int(digit)
print(s)    

#
number=int(input("Enter the number:"))#123
s=0
while number>0:
    digit=number%10#3|2|
    s+=digit
    number//=10#12|1|
print(s)

#4) Identify common elements between two lists.
l1=[1,2,3,4,5]
l2=[6,7,1,2,9]
common=[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)

#
L1=(list(map(int,input('Enter the elements in L1: ').split())))
L2=(list(map(int,input('Enter the elements in L2: ').split())))
L3=[]
for i in L1:
    if i in L2:
        L3.append(i)
print(L3)        



#5) Write a program that counts the number of words in a given string
input_str=input("Enter a string: ")
s=input_str.split()
n=len(s)
print(n)


#6) Sort a list of integers without using Python's sorted() function.
n=(list(map(int,input('Enter the elements: ').split())))
length=len(n)
for i in range(length):
    for j in range(0,length-i-1):
        if n[j] > n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)            


#7) Create a BankAccount class to simulate a bank account with features:
class BankAcc:
    def __init__(self,bal):
        self.bal=bal

    def deposit(self,amt):
        if amt>0:
            self.bal+=amt
            print(f"{amt} Amount deposited successfully.. balance:{self.bal}")
        else:
            print("Deposit amount must be positive...")

    def withdraw(self,amt):
        if amt>self.bal:
            print("Insufficient Balance...")
        else:
            self.bal-=amt
            print(f"{amt} Amount withdrawn successfully...balance:{self.bal}")

    def checkbalance(self):
        print(f"Balance: {self.bal}")

        
    
balance=int(input("Enter initial balance: "))
bank=BankAcc(balance)

dep_amt=int(input("Enter amount to deposit: "))
bank.deposit(dep_amt)

with_amt=int(input("Enter amount to withdraw: "))
bank.withdraw(with_amt)


bank.checkbalance()

#8 Check if a given string is a valid email address.
import re
email=input("Enter an email address: ")
email_pattern=r'^[a-z.A-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(email_pattern,email):
    print(f"'{email}' is a valid email address")
else:
    print(f"'{email}' is not a valid email address")

#9 Extract all phone numbers from a given text.

text=input()
ph_no=[]
for i in text:
    if i.isdigit():
        ph_no+=i
        print(i,end="")
print()

#10Extract all hashtags from a given text.

text=input()
for char in text:
    if char=="#":
        print(char,end='')
