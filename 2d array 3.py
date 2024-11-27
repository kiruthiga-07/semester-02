
#1
grades=[
    [85,78,92],
    [88,74,95],
    [91,82,89],
    [76,85,90]
    ]

print("Average grades for each student:")
for student in grades:
    stu_ave=sum(student)/len(student)
    print(f"student {grades.index(student)+1}: {stu_ave:.2f}")

print("higest grade in each subject:")
subjects=len(grades[0])
for i in range(subjects):
    highest_grade=max(grades[j][i] for j in range(len(grades)))
    if i==0:
        print(f"maths: {highest_grade}")
    elif i==1:
        print(f"science: {highest_grade}")
    else:
        print(f"english: {highest_grade}")

total_sum=0
total_grades=0
for student in grades:
    total_sum+=sum(student)
    total_grades+=len(student)
class_average=total_sum/total_grades
print(f"overall class average: {class_average:.2f}")
print()

#2
section_names=['A','B','C','D']
L=[
    [10,5,3,12],
    [6,8,2,0],
    [3,9,4,7],
    [14,7,5,10]
    ]

print("total quantities of each product:")
for i in range(len(L)):
    total_quantity=sum(L[i])
    print(f"product {i+1}: {total_quantity}")

          
product_index=2
quantities=L[product_index]
max_quantity=-1
section_index=-1
for i in range(len(quantities)):
          if quantities[i] > max_quantity:
              max_quantity=quantities[i]
              section_index=i
          
if 0 <= section_index < len(section_names):
          section_name=section_names[section_index]
          print(f"section with the highest quantity for product {product_index+1}: section {section_name}")
else:
    print(f"invalid section index: {section_index}")
          
lowest_quantity=sum(L[0])
lowest_product=0
for i in range(1,len(L)):
    total_quantity=sum(L[i])
    if total_quantity<lowest_quantity:
        lowest_quantity=total_quantity
        lowest_product=i
print(f"product with the lowest total quantity: product {lowest_product+1}")        
