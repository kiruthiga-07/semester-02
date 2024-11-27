#1
#a)adding new grade for a student
grades={'John':[80,85],'Alice':[92,88]}
student_name='John'
new_grade=95
if student_name in grades:
    grades[student_name].append(new_grade)
else:
    grades[student_name]=[new_grade]
print(grades)    

#b)calculating average grade for a student
grades={'John':[80,85,95],'Alice':[92,88]}
student_name='John'
if student_name in grades:
    average=sum(grades[student_name])/len(grades[student_name])
    print(f"{average:.2f}")
else:
    average='student name not found'
    
#c)removing student and all their grades
grades={'John':[80,85,95],'Alice':[92,88]}
student_name='John'
if student_name in grades:
    del grades[student_name]
else:
    print(f"student {student_name} not found. ")
print(grades)

#2
#a)create a tuple with a single element
se=(77,)
print(se)

#b)multiply a tuple by an integer
te=(1,2,3)
mt=te*3
print(mt)

#c)get the index of an element in a tuple
te=(10,20,30,40)
ie=te.index(30)
print(ie)

#d)modify an element in a tuple
te=(10,20,30,40)
L=list(te)
L[1]=25
modified_tuple=tuple(L)
print(modified_tuple)

#e)convert a tuple to a string
te=('hello','world')
ts=' '.join(te)
print(ts)

te=(1,2,3)
ts=str(te)
print(ts)

#f)find max and min values in a tuple
te=(10,20,30,40)
max_value=max(te)
min_value=min(te)
print(max_value)
print(min_value)

#g)count the occurances of an element in a tuple
te=(10,20,30,10,20)
ce=te.count(10)
print(te)

#h)create an nested tuple
nested_tuple=((1,2,3),(4,5,6),(7,8,9))
print(nested_tuple)

#i)access element in a nested tuple
nested_tuple=((1,2,3),(4,5,6),(7,8,9))
element=nested_tuple[2][1]
print(element)

#j) delete an element from a tuple
te=(10,20,30,40)
te=list(te )
s=te.remove(10)
a=tuple(te)
print(a)
