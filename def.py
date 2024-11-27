
#without argument and without return type
def add(x,y):
    ans=x+y
    print('add=',ans)
x=int(input())
y=int(input())
add(x,y)

#with argument and with return type
def add(x,y):
    ans=x+y
    return ans
x=int(input())
y=int(input())
print("add=",add(x,y))

#with argument and without return type
def add(x,y):
    ans=x+y
    print("add=",ans)
x=int(input())
y=int(input())
add(x,y)

#without argument and with return type
def add():
    x=int(input())
    y=int(input())
    ans=x+y
    return ans
ans=add()
print("add=",ans)
    
