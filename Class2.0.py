import json
import time 
college_records = []
Name_valid_char = [" ", '-', '\'']
Email_valid_char = ['@', '.']
Invalid = [ '@','!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
class Individual():
    name = " "
    email = " "
    id_number = " "
class Student():
    major = " "
class Instructor():
    insitution = " "
    degree = " "
class Validator(Individual, Student, Instructor):
    def type_of_user(self):
        while True:
            userinput = input("Are you a student or instructor?")
            if userinput == "student":
                Individual.name = input("Enter name:")
                try:
                    if Individual.name.isalpha():
                        Individual.id_number = input("Enter ID:")
                        if len(Individual.id_number) <= 7:
                            if int(Individual.id_number):
                                Individual.email = input("Enter Email:")
                                if not Individual.email.isalnum() and Individual.email not in Email_valid_char:
                                    Student.major = input("Enter your Major:")
                                    if Student.major.isalpha():
                                        return Student.major                   
                except:
                    ("Please enter your info again!")
            Repeat = input('Would you like to add another record? (Y,N)')
            if Repeat == 'N':
                break
            if userinput == "instructor":
                Individual.name = input("Enter name:")
                try:
                    if Individual.name.isalpha():
                        Individual.id_number = input("Enter ID:")
                        if len(Individual.id_number) <= 5:
                            if int(Individual.id_number):
                                Individual.email = input("Enter Email:")
                                if not Individual.email.isalnum() and Individual.email not in Email_valid_char:
                                    Instructor.insitution = input("Enter last college attended:")
                                    if Instructor.insitution.isalpha():
                                        Instructor.degree = input("Enter your highest degree recieved?")
                                        if Instructor.degree.isalpha():
                                            return Instructor.degree
                except:
                    ("Please enter your info again!")
            Repeat = input('Would you like to add another record? (Y,N)')
            if Repeat == 'N':
                break



        


y = Validator()

y.type_of_user()



college_records.append(y)
for college in college_records:
    print(f"Major: {college.major}")
    print(f"Name:{college.name}")
    print(f"ID: {college.id_number}")
    print(f"Email: {college.email}")
    print(f"Institution: {college.insitution}")
    print(f"Degree: {college.degree}")

    
        
