#1
def create_list(*args):
    return list(args)
result= create_list(2,'orange',2.45,True)
print(result)

#2
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num= int(input())
print(factorial(num))

#3
def product(a,b):
    return a*b
a=int(input())
b=int(input())
ans= product(a,b)
print(ans)

#4
def display_name(f_name,l_name):
    print(f"First name:{f_name},Last name:{l_name}")
first=input()
last=input()
display_name(first,last)

#5
def square_number():
    num=int(input())
    square=num*num
    print(square)
square_number()    
