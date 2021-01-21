'''
Create Character Variables for name and email validator!
'''
Name_valid_char = [" ", '-', '\'']
Email_valid_char = ['@', '.']
Invalid = [ '@','!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ] 
'''
Created a base class called Individual.
Inside the class I created a constructor to initialize 
the data members.
'''
class Individual():
    def __init__(self, name, email, id_number):
        self.name = name
        self.email = email
        self.id_number = id_number

    def DisplayInfo(self):
        print("Name:", name)
        print("Email:", email)
        print("ID:", id_number)
'''
Created a function within the class 
that displays the users input. 
Setting the parameter of the function to 
self which is a instance of the Individual class.
'''
'''
Created a student subclass that inherits the data members from the super class
by using the super() when working with multiple inheritance.
''' 
class Student(Individual):
    def __init__(self, name, email, id_number, major):
        super().__init__(name, email, id_number)
        self.major = major

    def DisplayInfo(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id_number )
        print("Current Major:", self.major)
        
'''
Used self method as a instance to display the individual class and
Student class to display the users info. 
'''
'''
Created a Instructor that asks users what institution
they attended and highest degree level. 
'''
class Instructor(Individual):
    def __init__(self, name, email, id_number, institution, Highest_degree):
        super().__init__(name, email, id_number)
        self.institution = institution
        self.Highest_degree = Highest_degree


    def DisplayInfo(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("ID:", self.id_number )
        print("Last College Enrolled:", self.institution)
        print("Highest Degree recieved:", self.Highest_degree)
'''
Create a validator that verifys if
 the user input is valid before adding
 it to the list. 
 I created 4 functions to vaildate the users input:
 1. Student ID
 Student must have 7 or less ints for ID.
 Created a try and except to verfiy the strs are ints.
 2. Instructor ID 
 Instructor must have 5 ints or less.
 Same algorithm as student.
 3. Name
 Name must be alpha and not contain invalid characters.
 4. Email
 Email must be alnum and only accept @ and " . ".
'''       
class Validator:                   
    def studentid(self):
        while True:
                    id_number = input("Enter ID:")
                    if len(id_number) <= 7:
                        try:
                            int(id_number)
                            return id_number
                        except:
                            print("Please enter ID!")

                            
    def instructorid(self):
        id_number = input("Enter ID:")
        if len(id_number) <= 5:
            try:
                int(id_number)
                return id_number
                
            except:
                print("Please enter ID!")            

    def type_of_name(self):
        while True:
            name = input("Enter your name:")
            if len(name) >= 0:
                bad_char = False
                for letter in name: 
                    if letter in Invalid:
                        bad_char = True
                        break
            if bad_char == False:
                return name
                    
    def type_of_email(self):
        while True:
            email = input("Enter your email:")
            for char in email:
                if char not in Email_valid_char and not email.isalnum():
                    return email
'''
Created a list called College Records.
Created a validator_instance.
1. ID 
2. Name
3. Email
Inside the condition statement 
If student they must enter their major.
After validating the users input I 
I created a student_instance implementing
the name, email, id, and major.
Then appended the instance to college records.
Same method for instructor except I used a
instructor_instance. 
'''
college_records = [] 
validator_instance = Validator()                        
while True:
    user = input("Student or Instructor")
    if user == "student":
        major = input("Current Major:")
        id_number = validator_instance.studentid()
        name = validator_instance.type_of_name()
        email = validator_instance.type_of_email()
        student_instance = Student(name , email , id_number, major)
        college_records.append(student_instance)
        
    elif user == "instructor":
        id_number = validator_instance.instructorid()
        name = validator_instance.type_of_name()
        email = validator_instance.type_of_email()
        Degree = input("Latest Degree:")
        institution = input("Last college attended:")
        instructor_instance = Instructor(name, email, id_number , Degree, institution)
        college_records.append(instructor_instance)
        
    Repeat = input('Would you like to add another record? (Y,N)')
    if Repeat == 'N':
        break
   

    
for coll in college_records:
    print(coll.DisplayInfo())
    
      
        









                
