
#1
rows,cols=map(int,input().split())
matrix1=[]
for _ in range(rows):
    matrix1.append(list(map(int,input().split())))

matrix2=[]
for _ in range(rows):
    matrix2.append(list(map(int,input().split())))

result=[[0 for _ in range(cols)]for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for row in result:
    print(" ".join(map(str,row)))

#2
n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()
for row in matrix:
    print(" ".join(map(str,row)))

#3
rows,cols=map(int,input().split())
matrix=[]
for _ in range(rows):
    matrix.append(list(map(int,input().split())))
max_value=0
for row in matrix:
    for element in row:
        if element>max_value:
            max_value=element
print("Maximum element=",max_value)            

#4
r,c=map(int,input().split())
if r!=c:
    print("Not a square matrix")
else:
    matrix=[]
    for _  in range(r):
        matrix.append(list(map(int,input().split())))
    symmetric=True
    for i in range(r):
        for j in range(i,r):
            if matrix[i][j]!=matrix[j][i]:
                symmetric=False
                break
        if not symmetric:
            break
    if symmetric:
        print("Symmetric matrix")
    else:
        print("Not symmetric matrix")
    
