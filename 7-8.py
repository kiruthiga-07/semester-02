
#1_subset
set1=set(input().split())
set2=set(input().split())
s=set1.issubset(set2)
print(s)

#2_slice the tuple
tup=(1,2,3,4,5,6,7,8)
sliced_tup=tup[2:6]
print(tup)
print(sliced_tup)

#3_unpack a tuple
t=('apple','banana','orange')
fruit1,fruit2,fruit3=t
print("fruit1 =",fruit1)
print("fruit2 =",fruit2)
print("fruit3 =",fruit3)

#4_remove all tuples
tuples=[(2,5),(9, ),(8,7,6),(4, ),(12,4,16,7)]
k=3
result=[ t for t in tuples if len(t)!=k]
print(result)

#5_single string
tuple_of_strings=('hello','world','python')
single_string=' '.join(tuple_of_strings)
print(single_string)

#6_list of tup to dict
list_of_tuples=[("a",1),("b",2),("c",3)]
dictionary=dict(list_of_tuples)
print(dictionary)

#7_pattern
for i in range(5,0,-1):
    print(' '*(5-i)+'* '*i)
for i in range(1,6):
    print(' '*(5-i)+'* '*i)
