d=dict(fruit="apple",veg="carrot",pet="cat")
print(d)
print(d.get("veg"))
print(d.keys())
d["age"]="30"
print(d)
print(d.values())
print(d.items())
d.update({"pet":"dog"})
print(d)
d['colour']='red'
print(d)
d.pop('veg')
print(d)
del d['fruit']
print(d)
for i in d:
    print(d[i])
x=d.setdefault("age",)
print(x)

