
#1
import random
print(random.randrange(1,20))
#2
import random
L=[12,13,56,70]
print(random.choice(L))
#3
import secrets
L=[12,13,56,70]
print(secrets.choice(L))
#4
import random
random.seed(2)#used to initialize
print(random.random())
#5
import random
L=[12,13,56,70,1,24,7]
print(random.choices(L,k=3))
#6
import random
L=[12,13,56,70,1,24,7]
random.shuffle(L)
print(L)
#7
import random
print(random.uniform(1,10))#generates with floating points with values

#8
import random
def start():
    print("*****ROCK PAPER SCISSOR*****")
    print("1 .STONE\n2 .PAPER\n3 .SCISSOR")
    print("Enter your choice:")
    user_choice=int(input())
    comp_choice=random.randint(1,4)
    print("\t")
    if comp_choice==1:
        print("Computer choice is: Rock")
    elif comp_choice==2:
        print("Computer choice is: Paper")
    else:
        print("Computer choice is: Scissor")
    if(user_choice==1 and comp_choice==3):
        print("YOU WON:)")
    elif(user_choice==2 and comp_choice==1):
        print("YOU WON:)")
    elif(user_choice==3 and comp_choice==2):
        print("YOU WON:)")
    elif(user_choice==comp_choice):
        print(".....IT'S A TIE.....")
    else:
        print("COMPUTER WON")
    play=input("Do you want to continue?Yes/No:")
    if play=="Yes":
        start()
    else:
        print("thanks for playing:)")
    
start()        

#password generate function
import random
import string

upper=string.ascii_uppercase
lower=string.ascii_lowercase
digits=string.digits
symbols=string.punctuation

def password_generator(size):
    chars=upper+lower+digits+symbols
    password=''
    for i in range(size):
        password+=random.choice(chars)
    return password
#execution starts here
dig=int(input())
print(password_generator(dig))

"""
import string
upper=string.ascii_uppercase
print(upper)

import string
lower=string.ascii_lowercase
print(lower)

import string
digits=string.digits
print(digits)

import string
symbols=string.punctuation
print(symbols)

