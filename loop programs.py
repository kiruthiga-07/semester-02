
#1)palindrome
num=int(input("Enter the num:"))#12321
num_str=str(num)
for i in range(len(num_str)//2):#5//2
    if num_str[i] != num_str[-(i+1)]:
        print(f"{num} is not a palindrome")
        break
else:
    print(f"{num} is a palindrome")

#2)sum of series
#1+x/1!+x^2/2!+.....x^n/n!
import math
x=int(input())#3
n=int(input())#5
sum_series=0
for i in range(x,n+1):#(3,5)
    term=math.pow(x,i)/math.factorial(i)
    sum_series+=term
print(f" The sum of the series:{sum_series:.4f}" )    

#3)product of the number
num=input()
product=1
for digit in num:
    product*=int(digit)
print(f"The product of the digits is:{product}")

#4)factorial
number=int(input())
factorial=1
for i in range(1,number+1):
    factorial*=i
print(f"the factorial of the number is:{factorial}")    

#5)prime or not prime
n=int(input())#5
if n<2:
    flag=False
else:
    flag=True#true
for i in range(2,n):#2,3,4
    if n%i==0:#5%2==0|5%3==0|5%4==0
        flag=False
        break
if flag:
    print("prime")
else:
    print("not prime")
  
#6
for i in range(5,9):#5|6|7|8
    print(i)

#7
for i in "python":#p y t h o n
    print(i,end=" ")

#8
for i in "python":#p?$|y?$|t?$|h?$|o?$|n?$
    print(i,'?$')

#9
x=8
while x<=20:#64|121|196|289|400
    print(x**2)
    x+=3   

#10)pattern
x=int(input())
y=int(input())
for i in range(x,y+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

#11)numbers from 100 to 500
x=int(input())
y=int(input())
for i in range(x,y):
    if i%11==0 and i%2!=0:
        print(i,end=" ")

 
