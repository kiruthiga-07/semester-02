#1
t=dict
d=[]
d=dict(name="kiruthiga",age="17",degree="Bsc",rollno="21")
print(d)

#2
print(d.keys())

#3                 
d.update({"age":"18"})
print(d)

#4
del d['name']
print(d)

#5
for i in dict.keys(d):
    print(i)
for i in dict.values(d):
    print(i)

#8
if "name" in d:
    print("true")
else:
    print("false")

#9
num=len(d)
print(num)

#10
x=d.get("age")
print(x)

#11
d.pop("age")
print(d)

#13
d.copy()
print(d)

#12
d.clear()
print(d)


