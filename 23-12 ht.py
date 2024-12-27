"""n1=int(input("Enter the number of elements to be inserted in L1: "))
n2=int(input("Enter the number of elements to be inserted in L2: "))
L1=(list(map(int,input('Enter the elements in L1: ').split())))
L2=(list(map(int,input('Enter the elements in L2: ').split())))
print("L1:",L1)
print("L2:",L2)
L3=[]
for i in L1:
    if i in L2:
        L3.append(i)
print(L3)        

#
num=input()
s=0
for i in num:
    s+=int(i)
print(s)

#
n=int(input())#5
n1=0
n2=1
count=0
if n<=0:
    print('enter a positive number')
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1,end=' ')#0,1,1,2,3
        n3=n1+n2#0+1=1|1+1=2|1+2=3|2+3=5|3+5=8
        n1=n2#1|1|2|3|
        n2=n3#1|2|3|5|8
        count+=1#1|2|3|4|5
   
#
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")

#
num=int(input())
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print("It is prime")
else:
    print("Not a prime")

#
n=input()
s=n[::-1]
if n==s:
    print("palindrome")
else:
    print("not a palindrome")

#
num=int(input())
for i in range(1,num+1):
    print('*'.join(str(i)for _ in range(i)))
for i in range(num,0,-1):
    print('*'.join(str(i)for _ in range(i)))

#
for i in range(5,0,-1):
    print(" "*(5-i)+"* "*i)
for i in range(1,6):
    print(" "*(5-i)+"* "*i)

#
row=int(input())
column=int(input())
for i in range(row):
    for j in range(column):
        print("*",end=' ')
    print()    


#
n=int(input())
n_str=str(n)
for i in range(len(n_str)//2):
    if n_str[i]!=n_str[-(i+1)]:
        print("not a palindrome")
        break
else:
    print("palindrome")

#
n=int(input())
sum_digit=0
num=n
while n!=0:
    rem=n%10
    sum_digit+=(rem**3)
    n//=10
if sum_digit==num:
    print('armstrong number')
else:
    print('not an armstrong number')


#
num=int(input())
while num!=0:
    first=num//100
    second=(num//10)%10
    third=num%10
    reverse=third*100+second*10+first
    print(reverse)
    break    
 """
#
even=0
odd=0
arr=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)























































    
