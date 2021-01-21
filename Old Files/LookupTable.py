# Create a program that takes clients info/ append to dictionary/ encrypt
from cryptography.fernet import Fernet
from getpass import getpass
from os.path import exists

import json
Employee_records = {}
class employee:
    def __init__(self, name, age, gender, race):
        self.name = name
        self.age = age
        self.gender = gender 
        self.race = race
    def employee_name(self):
        while True:
            name = input("Name:")
            Invalid_chars = [" ", "\'", " - "]
            if len(name) == 0:
                continue
            bad_char = False
            for letter in name:
                if letter.isalpha() and letter not in Invalid_chars:
                    Employee_records["Name"] = name
                    bad_char = True
            break
    def employee_age(self):
        while True:
            age = input("Age:")
            if len(age) == 0:
                continue
            bad_char = False
            if len(age) <= 2:

                try:
                    if age.isdigit():
                        Employee_records["Age"] = age
                    elif age.isalpha():
                        continue
                    bad_char = False
                except: 
                    print("Please enter your age!")
            break
    def employee_gender(self):
        while True:
            gender = input("Gender:")
            if gender == "male" or gender == "Male":
                Employee_records["Gender"] = gender
            elif gender == "female" or gender == "Female":
                Employee_records["Gender"] = gender
            break
    def employee_race(self):
        race = input("Enter your ethincity:\n African American\n Caucasian\n Asian\n Mexican\n")
class IT(employee):
    def __init__(self, id):
        self.id = id

    def IT_id(self):
        id = input("ID:")
        if len(id) <= 7:
            try:
                int(id)
                Employee_records['ID'] = id
            except:
                print("Please print ID!")

record = employee(" ", " ", " ", " ")
record.employee_name()
record.employee_age()
record.employee_gender()
record.employee_race()
IT = IT(" ")
IT.IT_id()
print(Employee_records)












