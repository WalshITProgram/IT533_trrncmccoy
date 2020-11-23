import json
import time 
college_records = []
Name_valid_char = [" ", '-', '\'']
Email_valid_char = ['@', '.']
Invalid = [ '@','!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
class Individual():
    def __init__(self):
        self.userinput = input()
class Student():
    def __init__(self):
        self.identity = input("Are you a student or instructor? ")
        self.userid = input("Enter your user id:")
        self.username = input("Enter your name:")
        self.useremail = input("Enter your email address:")
        self.usermajor = input("Enter the current program you are enrolled in?")
    
    def get_user_input(self):
        while True:
            try:
                identity = input("Are you a student or instructor? ")
                if len(identity) == 0:
                    continue
                    bad_char = False
                if identity.isalpha() and identity == "student":
                    return identity 
            except:
                print('Invalid input!')
    
    def get_user_name(self):
        while True:
            username = input("Enter your name:")
            if len(username) == 0:
                continue
            bad_char = False
            for letter in username:
                if letter not in Name_valid_char and not letter.isalpha():
                    bad_char = True
            if bad_char == False:
                return username
                break

    def get_user_email(self):
        while True:
            user_email = input("Enter your email address:")
            if user_email == 0:
                continue
            bad_char = False 
            for email in user_email:
                if email not in Email_valid_char and not user_email.isalnum:
                    bad_char = True
            if bad_char == False:
                return user_email
            
            
    def userID(self):
        while True: 
            userid = input("Enter your user id:")
            if len(userid) <= 7:
                try:
                    int(userid)
                    return userid
                except:
                    print("Please enter user id!")

    def studentmajor(self):
        while True:
            try:
                userprogram = input("Enter the current program you are enrolled in?")
                if len(userprogram) == 0:
                    continue
                bad_char = False 
                if userprogram.isalpha(): 
                    bad_char = True
                    return userprogram
            except:
                print("Please enter current program!")
class Instructor():
    def __init__(self):
        self.instructor_name = input("Enter teachers your name:")
        self.instructor_id = input("Enter your user id:")
        self.institution = input("Enter your last institution you graduated from:")
        self.degree = input("Your highest level of education:")
        self.instructor_email = input("Enter your email address:")
    
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
class Validator():
    def __init__subclass(self, college_records_dict_, cls):
        self.college_records_dict_ = college_records
        cls.college_records_dict_ = college_records
    def display(self):
'''





y = Student()
y.get_user_input()
y.get_user_name()
y.get_user_email()
y.userID()
y.studentmajor()
z = Instructor()
z.teacher_name()
z.teacher_id()
z.teacher_college()
z.teacher_degree()
z.teachers_email()
print(z.__dict__)

user = input("Student or Instructor?")
if user == "Student":
    student. 


z.student()
          



            
        
 
 


                








