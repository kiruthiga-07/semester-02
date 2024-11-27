
#students and grades
N1=int(input("Enter the number of students:"))
student_names=[]
for i in range(N1):
    student_name=input("Enter a student name:")
    student_names.append(student_name)    
N2=int(input("Enter the number of grades:"))
student_grades=[]
for i in range(N2):
    student_grade=input("Enter a grade:")
    student_grades.append(student_grade)
if  N1!=N2:
    print("Error: The number of students and number of grades must be the same.")
else:
    for i in range(N1):
         print(f"{student_names[i]}  {student_grades[i]}")

#minimum
import array as arr
n=arr.array('i')
a=int(input("Enter the number of elements to be inserted:"))
for i in range(a):
    n.append(int(input()))
print(n)
minimum=n[0]
for i in n:
    if i<minimum:
        minimum=i
print("minimum element=",minimum)        

#sort and merge
import array as arr
n1=arr.array('i')
x=int(input("Enter the number of elements to be inserted:"))
for i in range(x):
    n1.append(int(input()))
n1=n1.tolist()    
print(n1,end=" ")    
print()

n2=arr.array('i')
y=int(input("Enter the number of elements to be inserted:"))
for i in range(y):
    n2.append(int(input()))
n2=n2.tolist()    
print(n2,end=" ")
print()
n1.extend(n2)
print(n1)
n1.sort(reverse=True)
print(n1)


