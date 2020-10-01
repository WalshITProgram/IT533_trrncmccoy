# Create Variables for Username
first_name = input("First Name:")
last_name = input("Last Name:")
# Create the structure of the username 
username = first_name[:4] + last_name[:4]
user1 = username.isalpha()
# Create Variables for Password. User inputs passwords and passcode generates a random item

Passcode = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '+']
# Create and Import random.choice for Passcode
import random
import math

# Create Username generator
def username_generator(first_name, last_name):
    if username[:4] == first_name[:4] and username[4:8] == last_name[:4] and user1:
        return username  
        if len(username) >= 7:
            print(username)
    elif len(username) < 10:
        print("Please Enter Username:")
print(username_generator(first_name, last_name)) 
# Create Variables for Password. User inputs passwords and passcode generates a random item
Pass = input("Enter Password:")
Pass_item = random.choice(Passcode) 
Pass_team = Pass + Pass_item
Pass1 = Pass_team.isalpha()
Passcode = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '+']

def user_password(Pass, Pass_team):
    if len(Pass_team) > 12:
        return Pass_team 
        print(Pass_team)
    elif len(Pass_team) < 12:
        print("Please Enter Password:")
print(user_password(Pass, Pass_team))