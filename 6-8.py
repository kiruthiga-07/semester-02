
#1_majority
N=int(input())#7
arr=list(map(int,input().split()))#1 2 3 3 3 3 10
x=int(input())#4
count=arr.count(x)#0
if count>N/2:#0>3.5?
    print(f"{x} is a majority element")
else:
    print(f"{x} is not a majority element")

#2_second largest
n=int(input("Enter the number of element in the array: "))#6
array=list(map(int,input("Enter the elements seperated by spaces: ").split()))#12 35 1 10 34 1
if len(array)<2:
    print("Array must contain at least two elements")
else:
    largest=float("-inf")
    second_largest=float("-inf")
    for num in array:#12 35 1 10 34 1
        if num>largest:#12>f("-inf")|35>12|1>35|1>12|10>35|10>12|34>35|34>12
            second_largest=largest#f("-inf")|12|34
            largest=num#12|35
        elif num>second_largest and num!=largest:
            second_largest=num
    if second_largest==float("-inf"): 
         print("There is no second largest element")
    else:
         print(f"The second largest number is {second_largest}")

#3_replacing numbers     
number=input("Enter the phone number: ")
to_replace=input("Enter the digit to be replace: ")
replace_with=input("Enter the digit to replace with: ")
if len(to_replace)!=1 or len(replace_with)!=1:
    print("Both the digit to be replace and digit to be replace with must be single characters.")
else:
    modified_number=number.replace(to_replace,replace_with)
    print(f"Modified_number = {modified_number}")
  

#4_username and password
login_details={
    "user1":"password123",
    "user2":"12345678",
    "user3":"password"
    }
username=input("Enter the username: ")
password=input("Enter the password: ")
if username not in  login_details:
    print("Invalid username")
elif login_details[username]!=password:
    print("Incorrect password")
else:
    print("Successfully logged in.")







