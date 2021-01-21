import json
import time 
college_records = []
Name_valid_char = [" ", '-', '\'']
Email_valid_char = ['@', '.']
Invalid = [ '@','!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
class Individual():
    def __init__(self):
        self.identity = " "
        self.id = " "
        self.name = " "
        self.email = " "
class Student():
    def __init__(self):
        self.major = " "
class Instructor():
    def __init__(self):
        self.degree = " "
        self.institution = " "
class Validator(Individual, Student, Instructor):   
    def get_user_input(self):
        while True:
            Individual.identity = input("Are you a student or instructor? ")
            try:
                if Individual.identity == "student":
                    return Individual.identity 
                if Individual.identity == "instructor":
                    return Individual.identity 
            except:
                print('Invalid input!')
            
    def userID(self):
        while True:
            if Individual.identity == "student":
                Individual.id = input("Enter your user id:")
                if len(Individual.id) <= 7:
                    try:
                        int(Individual.id)
                        return Individual.id
                    except:
                        print("Please enter user id!")
            
    def get_user_name(self):
        while True:
            Individual.name = input("Enter your Name:")
            if len(Individual.name) == 0:
                continue
            bad_char_hit = False
            for letter in Individual.name:
                if letter not in Name_valid_char and not letter.isalpha():
                    bad_char_hit = True
            if bad_char_hit == False:
                break
                
    def get_user_email(self):
        while True:
            if Individual.name.isalpha():
                Individual.email = input("Enter your email address:")
                if Individual.email == 0:
                        continue
                bad_char = False 
                for email in Individual.email:
                    if email in Email_valid_char and Individual.email.isalnum:
                        return Individual.email
            
    
    def studentmajor(self):
        while True:
            try:
                Student.major = input("Enter the current program you are enrolled in?")
                if len(Student.major) == 0:
                    continue
                bad_char = False 
                if Student.major.isalpha(): 
                    return Student.major
            except:
                print("Please enter current program!")
            
        
   

x = Validator()
x.get_user_input()
x.userID()
x.get_user_name()
x.get_user_email()
x.studentmajor()
college_records.append(x.get_user_input())
college_records.append(x.userID())
college_records.append(x.get_user_name())
college_records.append(x.get_user_email())
college_records.append(x.studentmajor)
for college in college_records:
    print(college.identity)
    print(college.id)
    print(college.name)
    print(college.email)
    print(college.major)
Repeat = input('Would you like to add another record? (Y,N)')
if Repeat == 'N':
    bad = True
'''  
    def teacher_name(self):
        while True:
            instructor_name = input("Enter your name:")
            if len(instructor_name) == 0:
                continue
            bad_char = False
            for name in instructor_name:
                if name not in Name_valid_char and not name.isalpha():
                    bad_char = True
            if bad_char == False:
                return instructor_name
                break

    def teacher_id(self):
        while True:
            instructor_id = input("Enter your id:")
            if len(instructor_id) <= 5:
                try:
                    int(instructor_id) 
                    return instructor_id
                except:
                    print("Please enter your id!")
    def teacher_college(self):
        while True:
            institution = input("Enter your last institution you graduated from:")
            if len(institution) == 0:
                continue
            bad_char = False
            for college in institution:
                if college.isalpha() and college not in Invalid:
                    bad_char = True
                    return institution
    def teacher_degree(self):
        while True:
            degree = input("Your highest level of education:")
            if len(degree) == 0:
                continue
                bad_char = False
            for level in degree:
                if level.isalpha() and level not in Invalid:
                    bad_char = True
                    return degree
    def teachers_email(self):
        while True:
            instructor_email = input("Enter your email address:")
            if len(instructor_email) == 0:
                continue
                bad_char = False
            for email in instructor_email:
                if email.isalnum and email in Email_valid_char:
                    bad_char = True
                    return instructor_email
'''








          



            
        
 
 


                








