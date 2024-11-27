
#1)temperature
size=int(input("Enter the size of the array: "))
temperatures=list(map(int,input("Enter the elements of the array seperated by spaces:").split()))
negative_temps=[]
positive_temps=[]
for temp in temperatures:
    if temp<0:
        negative_temps.append(temp)
    else:
        positive_temps.append(temp)

negative_temps.extend(positive_temps)
print("Rearranged_temp:",negative_temps)

#2)pattern
num_rows=int(input("Enter the number of rows: "))
current_char=ord('A')
for i in range(num_rows):
    for j in range(i+1):
 9o       print(chr(current_char),end=" ")
        current_char+=1
    print()

#3
for x in range (10,20):
    if x%2==0:
        continue
        print(x)
        
#4)convert to for loop
x=3
for x in range(3,9,2):
    print(x*10)

#5)duplicate IDs
n=int(input("Enter the number of elements to be inserted:"))
l=[]
encountered_id=[]
duplicate_id=[]
for i in range(n):
    d=int(input())
    l.append(d)
for user_id in l:
    if user_id in encountered_id:
        duplicate_id.append(user_id)
   
print(*duplicate_id)        
