
#1
import random
def roll_dice():
    return random.randint(1,6)
def main():
    while True:
        user_input=input("Type 'roll' to roll the dice or 'exit' to quit:").lower()
        if user_input=='roll':
            print(f"You rolled a {roll_dice()}!")
        elif user_input=='exit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. please type 'roll' or 'exit'.")
main()
      
#2
import random
restaurants=[
    "Palm shore",
    "Faizee",
    "Madurai kannapar",
    "Udupi",
    "Junior kuppana",
    "A2B",
    "Copper kitchen",
    "Grill box"
    ]
def pick_restaurant():
    return random.choice(restaurants)

def main():
    while True:
        user_input=input("Type 'pick' to choose a restaurant or 'bye' to exit:").lower()
        if user_input=='pick':
            print(f"Tonight, you are going to {pick_restaurant()}!")
        elif user_input=='bye':
            print("Goodbye! Enjoy your dinner!")
            break
        else:
            print("Invalid input. please type 'pick' or 'bye'.")
main()

#3
import re
def validate_username(username):
    if not re.match("^[A-Za-z0-9_]+$", username):
        return False,"Must conatin only letters, numbers, or undrscores."
    if not re.match("^[A-Za-z]", username):
        return False,"Must start with a letter."
    if not(5<=len(username)<=15):
        return False,"Must be between 5 and 15 characters."
    return True,"Useraname is valid."
def check_username():
    username=input("Enter a username:")
    valid,message=validate_username(username)
    if valid:
        print(message)
    else:
        print(f"Validation failed: {message}")
check_username()        
