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
class Student(Individual):
    def __init__(self, username, useremail, usermajor, userid):
        self.name = username
        self.email = useremail
        self.major = usermajor
        self.id_number = userid
        

    def student_major(self):
        while True:
            usermajor = input("Enter Students Major:")
            if usermajor.isalpha():
                return usermajor
                
def type_of_user():
    while True:
        user = input("Are you a student or instructor?")

        if user == "student":
            if "student":
                student_instance = Student(" ", " ", " ", " ")
                college_records.append(student_instance)
                userid = input("Enter ID:")
                if len(userid) <= 7:
                    try:
                        int(userid)
                        return userid
                        
                    except:
                        print("Please enter ID!")
                        
        if user == "instructor":
            if "instructor":
                instructor_instance = Instructor(" ", " ", " ", " ")
                college_records.append(instructor_instance)
                teacherid = input("Enter ID:")
                if len(teacherid) <= 5:
                    try:
                        int(teacherid)
                        break
                    except:
                        print("Please enter ID!")

def type_of_name():
    while True:
        name = input("Enter your name:")
        if name.isalpha() == True:
            return name
def type_of_email():
    while True:
        email = input("Enter your email:")
        for char in email:
            if char not in Email_valid_char and not email.isalnum():
                return email

class Instructor(Individual):
    def __init__(self, teachername, teacheremail, teachercollege, teacher_degree):
        self.name = teachername
        self.email = teacheremail
        self.college = teachercollege
        self.degree = teacher_degree
    def instructor_college(self):
        while True:
            teachercollege = input("Enter your last college you were enrolled in: ")
            if teachercollege.isalpha() == True:
                return teachercollege
    def instructor_degree(self):
        while True:
            teacher_degree = input("Enter your highest degree received:")
            if teacher_degree.isalpha() == True:
                return teacher_degree
class Validator(Individual):
    def displayinformation():

        return display 

                    
          
student_instance = Student(" ", " ", " ", " ")
student_instance.id_number = type_of_user()
student_instance.name = type_of_name()
student_instance.email = type_of_email()
student_instance.student_major()

college_records.append(student_instance)
for college in college_records:
    print(college.name)
    print(college.email)
    print(college.student_major())
    print(college.id_number)
instructor_instance = Instructor(" ", " ", " ", " ")
instructor_instance.name = type_of_name()
instructor_instance.email = type_of_email()
instructor_instance.instructor_college()
instructor_instance.instructor_degree() 
college_records.append(instructor_instance)
for teacher in college_records:
    print(teacher.name)
    print(teacher.email)
    print(teacher.teachercollege)
    print(teacher.degree)
    print(teacher.teacherid)
'''
Define variable inside of class
Three Classes:
Individual 
    ID 
    Name 
    Email

Student 
    Major
Teacher 
    College
    Highest Degree Earned 
'''




                
