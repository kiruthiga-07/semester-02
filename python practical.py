
#1 temperature convertion
print("Enter 'c' to convert Celsius to Fahrenheit")
print("Enter 'f' to convert Fahrenheit to Celsius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input("Enter temperature in Celsius:"))
    fahrenheit=(celsius*9/5)+32
    print('%.2f Celsius is: %0.2f Fahrenheit'%(celsius,fahrenheit))
elif choice=='f':
    fahrenheit=float(input('Enter temperature in Fahrenheit:'))
    celsius=(fahrenheit-32)*5/9
    print('%.2f Fahrenheit is: %0.2f Celsius'%(fahrenheit,celsius))
else:
    print('Invalid Input')

#2 student mark processing
a=int(input('Enter the marks obtained insubject 1:'))
b=int(input('Enter the marks obtained insubject 2:'))
c=int(input('Enter the marks obtained insubject 3:'))
d=int(input('Enter the marks obtained insubject 4:'))
e=int(input('Enter the marks obtained insubject 5:'))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")

#3 find the area of rectangle,square,triangleand circle
#area of Rectangle
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
area_rec=l*b
print(f"the area of rectangle is: {area_rec}")
print()

#area of Square
s=int(input("enter the side of the square:"))
area_sq=s*s
print(f"the area of the square: {area_sq}")
print()

#area of triangle
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle: "))
area_tri=1/2*b*h
print(f"the area of the triangle: {area_tri}")
print()

#area of circle
pi=3.14
r=int(input("Enter the radius of the radius:"))
area_cir=pi*r*r
print(f"the area of the circle: {area_cir}")
print()


#4 fibonacci series
n=int(input())
n1=0
n2=1
count=0#1|2|3|4|
if n<=0:
    print("enter a positive integer")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1,end=" ")
        n3=n1+n2#0+1=1|1+1=2|1+2=3|2+3=5
        n1=n2#1|1|2
        n2=n3#1|2|3
        count+=1
print()






















    
    
