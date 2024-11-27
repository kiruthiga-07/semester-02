"""
#1
rows=int(input())
cols=int(input())
sales_data=[]
for i in range(rows):
    row=list(map(int,input().split()))
    sales_data.append(row)
print(sales_data)    
total_sales=0
for row in sales_data:
    total_sales+=sum(row)
print(total_sales)    

#2
rows=int(input())
cols=int(input())
board=[]
for i in range(rows):
    row=list(map(int,input().split()))
    board.append(row)
to_find=int(input())
flag=False
for i in range(rows):
    for j in range(cols):
        if board[i][j]==to_find:
            print(f"found at({i},{j})")
            flag=True
            
  
if not flag:
    print("not found")
        
#3
n=int(input())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
print("Transpose matrix is:")    
for i in range(n):
    for j in range(n):
        print(arr[j][i],end=" ") 
    print()

#4
rows=int(input())
cols=int(input())
seating_chart=[]
for i in range(rows):
    row=list(map(int,input().split()))
    seating_chart.append(row)
print("Theatre ceating chart:")
for i in range(rows):
    for j in range(cols):
        if seating_chart[i][j]==0:
            print("O",end=" ")
        else:
            print("X",end=" ")
    print()
    """
m=int(input())
n=int(input())
a=[]
for _ in range(m):
    l=list(map(int,input().split()))
    a.append
print(l)    
    

