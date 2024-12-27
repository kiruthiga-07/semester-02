#temperature conversion
print("Enter c to convert celsius to fahrenheit")
print("Enter f to convert fahrenheit to celius")
choice=input("Enter your choice: ")
if choice=="c":
    celsius=float(input("Enter tempearture in celsius: "))
    fahrenheit=(celsius*9/5)+32
    print("%.2f Celsius is: %0.2f Fahrenheit"%(celsius,fahrenheit))
elif choice=="c":
    fahrenheit=float(input("Enter tempearture in fahrenheit: "))
    fahrenheit=(celsius-32)*5/9
    print("%.2f Fahrenheit is: %0.2f Celsius"%(fahrenheit,celsius))
else:
    print("Invalid input")
print()    

#palindrome
n=input("Enter any word:")
s=n[::-1]
if n==s:
    print("palindrome")
else:
    print("Not a palindrome")
