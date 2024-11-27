#1
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
rows=len(arr)
cols=len(arr[0])
for j in range(cols):
    if j%2==0:
        for i in range(rows):
            print(arr[i][j],end=" ")
    else:
        for i in range(rows-1,-1,-1):
            print(arr[i][j],end=" ")
print()


