import array as s
n=s.array('i')
add=0
a=int(input("Enter the number of elements to be inserted: "))
for i in range(a):
    n.append(int(input()))
print(n)

for d in range(a):
    add+=n[d]
print("Sum of numbers:",add)

count=0
p=int(input())
for u in n:
    if u==p:
        count+=1
print(count)

maximum=n[0]
for i in n:
    if i>maximum:
        maximum=i
print(maximum)



    
