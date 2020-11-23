import json
import time 
college_records = {}
valid_char = ['@']
Invalid = [ '@','!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
class Student():
    def __init__(self, identity, name, id, email, major, staff):
        self.identity
        self.name
        self.id
        self.email
        self.major
        self.teacher
        self.student
    def username(self, typeinput):
        while True:
            info_school = input(typeinput)
            if len(info_school) == 0:
                continue
            bad_char = False
            if typeinput == "Instructor":
                for c in info_school:
                    if not c.isalpha() and c not in Invalid:
                        bad_char = True
            if typeinput == "Student":
                for ch in info_school:
                    if not ch.isalpha() and ch not in Invalid:
                        bad_char = True
            if info_school.isalpha() and info_school == "student":
                try:
                    str(info_school)
                except:
                    print("Please enter student or instructor:")

    def userID(self, staff_dict):
        while True:
            studentID = input("Enter User ID")
            if len(studentID) == 0:
                continue
            bad_char = False
            if len(studentID) <= 7:
                try:
                    int(studentID)
                    staff_dict['ID'] = studentID
                    break
                except:
                    print("Please enter ID")
    def major(self, staff_dict):
        while True:
            Program = input("Enter your Major:")
            if len(Program) == 0:
                continue 
            bad_char = False
            for l in Program: 
                if l not in Invalid and not l.isalpha():
                    bad_char = True
            if bad_char == False:
                staff_dict["Program"] = Program
    def email(self, staff_dict):
        while True:
            Email_add = input("Enter Email Address:")
            if len(Email_add) == 0:
                continue
            bad_char = False
            for char in Email_add:
                if char not in valid_char and not char.isalnum():
                    bad_char = True 
                if bad_char == False:
                    staff_dict['Email'] = Email_add
                    break
class instructor():
    def staff(self, staff_dict):
        while True:
            teacher = input("Enter student or instructor:")
            if len(teacher) == 0:
                continue
            bad_char = False
            if teacher.isalpha() and teacher == "instructor":
                try:
                    str(teacher)
                except:
                    print("Please Enter Student or Instructor!")
            for char in teacher:
                if char not in Invalid and not char.isalpha():
                    bad_char = True
    def teacher_id(self, staff_dict):
        while True:                
            teacherID = input("Please enter ID:")
            if len(teacherID) >= 5:
                try:
                    int(teacherID)
                    staff_dict['ID'] = teacherID
                except:
                    print("Please enter ID number:")
    def school_name(self, staff_dict):
        while True:
            Institution = input("Please enter name of school:")
            if len(Institution) == 0:
                continue
            bad_char = False
            if Institution.isalpha(): 
                for let in Institution:
                    if let not in Invalid and let.isalpha():
                        bad_char = True 
                    if bad_char == False:
                        staff_dict['School'] = Institution
    def education_degree(self, staff_dict):
        while True:
            Degree = input("Enter Highest Degree Level:")
            if len(Degree) == 0:
                continue
            bad_char = False
            if Degree.isalpha():
                for lett in Degree:
                    if lett not in Invalid and lett.isalpha():
                        bad_char = True
                    if bad_char == False:
                        staff_dict["Degree"] = Degree
                        break
    def name(self, staff_dict):
        while True:        
            Teacher_Name = input("Enter Name:")
            if len(Teacher_Name) == 0:
                continue
            bad_char = False
            for letter in Teacher_Name:
                if letter not in Invalid and not letter.isalpha():
                    bad_char = True
                if bad_char == False:
                    staff_dict["Teachers Name"] = Teacher_Name
                    break
'''
while True:
    college_records = {}
    user_info(staff_dict)
    userID(staff_dict)
    major(staff_dict)
    email(staff_dict)
    staff(staff_dict)
    teacher_id(staff_dict)
    school_name(staff_dict)
    education_degree(staff_dict)
    name(staff_dict)
    college_records.append(staff_dict)
    Repeat = input("Would you like to add another record?")
    if Repeat == 'N':
        break
'''