import re
def verify_password(password):
    ex=r'^(?=.+[a-z])((?=.+[A-Z]){3,})(?!.[0-9])(?!.[(!@#$%^&*()_+-=)]).{12}$'
    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")
password=input("Enter the password: ")
verify_password(password)
