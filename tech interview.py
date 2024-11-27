"""
#for loop
for i in range(1,5):
    print(i)

#while loop
i=1
while i<=5:
    print(i)
    i+=1


while True:
    name=input("Enter your name: ")
    if name.isalpha():
        print(name)
        break
    else:
        print("Invallid input. Please enter only letters")
#condititional statement
age=int(input())
if age<18:
    print("The child is minor")
elif age==18:
    print("The child just became adult")
else:
    print("You are an adult")

#finding factors using for loop
n=int(input())
fact=[]
for _ in range(n):
    fact.append(int(input()))
new_fact=[]
for i in fact:   
    if i>0 and n%i==0:
        new_fact.append(i)
print(new_fact)

n=[1,2,3,4,5]
s=sum(n)
print(s)

def greet(name):
    print(f"Hello, {name}")

name=input()
greet(name)

def add_num(a,b):
    return a+b
n1=int(input())
n2=int(input())
result=add_num(n1,n2)
print(result)

username="Dharshini"
password="12345"
if username== and password=="12345":
    print("Access Granted")
else:
    print("Access Denied....")


value=input("Enter the numbers: ")
if value.isdigit():
    print("You entered the valid number")
else:
    print("Invalid Input")

import array as arr
n=arr.array('i')
x=int(input())
for i in range(x):
    n.append(int(input()))
print(n)

import array as arr
a=arr.array('i',[23,4,5])
print(a*3)

import array as arr
a=arr.array('i',[i*6 for i in range(1,7)])
print(a)

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


n=int(input()) #3
for i in range(n): #0 1 2 
    for j in range(n):
        if i==n-1 or j==n-1:
            print('* ',end="")
        else:
            print(' ',end=" ")
    print()

#to print * in 
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('* ',end="")
        else:
            print(' ',end=" ")
    print()

#to print * in middle row
n=int(input())
for i in range(n):
    for j in range(n):
        if i==1 and j==1 and i==n-2 and j==n-2:
            print('* ',end="")
        else:
            print(' ',end=" ")
    print()


#to print * in last row
n=int(input())
for i in range(n):
    for j in range(n):
        if i==n-1 and j==1:
            print('# ',end="")
        else:
            print(' ',end=" ")
    print()


n=int(input())#153
sum_dig=0
num=n#153
while n!=0:#
    rem=n%10#153%10=3|15%10=5|1
    sum_dig+=(rem**3)#0+(3**3)=27|27+(5**3)=152|152+(1**3)=153
    n//=10#15|1|0
if sum_dig==num:
    print("Armstrong number")
else:
    print("Not Armstrong number")


num=int(input())
limit=int(input())
multiples=[]
for i in range(1,limit+1):
    if i%num==0:
        multiples.append(i)
print(multiples)        

"""









