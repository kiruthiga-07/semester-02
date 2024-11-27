#1
def student_details(name,age,department):
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print(f"Student Department: {department}")
    
student_name= input("Enter the student name:")
student_age=int(input("Enter the student age:"))
student_department=input("Entre student department:")

student_details(name=student_name,age=student_age,department=student_department)
print()

#2
def food_details(food_dict):
    print(f"Food Type: {food_dict.get('food_type')}")
    print(f"Item Name: {food_dict.get('item_name')}")
    print(f"Item Cost: {food_dict.get('item_cost')}")

food_type =input("Enter the food type: ")
item_name =input("Enter the item name: ")
item_cost=float(input("Enter the item cost: "))

food_dict={
    'food_type': food_type,
    'item_name': item_name,
    'item_cost': item_cost
    }
food_details(food_dict)
