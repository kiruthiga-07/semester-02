#1
first_name=input("Enter first name:")
output_str=""
for char in first_name:
    if not char.isdigit():
        output_str+=char
print("Hi! Your entered input is:",output_str)        


#2
first_name=input("Enter first name:")
letters=""
spl_chars=""
for char in first_name:
    if char.isalpha():
        letters+=char
    elif not char.isdigit():
        spl_chars+=char
print("Your entered characters are:",letters)
print("Your entered special characters are:",spl_chars)
