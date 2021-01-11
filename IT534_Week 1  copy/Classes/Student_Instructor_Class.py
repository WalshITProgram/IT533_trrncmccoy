class Person():

    def __init__(self, name, email, id, program, degree, institution):
        self.name = name
        self.email = email
        self.id = id
        self.program = program
        self.degree = degree
        self.institution = institution

    def displayInformation(self):
        print("Name: " + self.name)
        print("Email: " + self.name)
        print("ID: " + self.id)

class Student():

    def __init__(program):
        self.program = program

    def displayInformation():
        print("Program: " + self.program)

class Instructor():

    def __init__(degree, institution):
        super().__init__(name, email, id, degree, institution)
        self.degree = degree
        self.institution = institution

    def displayInformation():
        print("Degree: " + self.degree)
        print("Institution: " + self.institution)

class Validator():

    def __init__(self):
        self.validate_name = ['!','"','@','#','$','%','^','&','*','(',')','_','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']
        self.validate_email = ['!','"','\'','#','$','%','^','&','*','(',')','=','+',',','<','>','/','?',';',':','[',']','{','}','\\']


    def validate_name(self, passed_name):
        if passed_name and str:
            has_bad_chars = False
            for character in passed_name:
                if character in validate_name:
                    return True 
                else:
                    return False
        else:
            print("Your name cannot be blank")
            return False
    
    def validate_email(self, passed_email):
        if passed_email and str:
            has_bad_chars = False
            for character in passed_email:
                if character in validate_email:
                    has_bad_chars = True
                else:
                    has_bad_chars = False
            if not has_bad_chars:
                return True 
            else:
                print("Your email has bad characters in it")
                return False
        else:
            print("Your email cannot be blank")
            return False 

    def validate_user_type(self, passed_type):
        if passed_type.lower == "s" or passed_type.lower == "i":
            return True
        else:
            print("The provided user type is invalid")
            return False

    def validate_student_id(self, passed_id):
        if passed_id.len() <= 7 and int(passed_id):
            return True
        else:
            print("The provided student ID is invalid")
            return False
    
def validate_instructor_id(self, passed_id):
    if passed_id.len() <= 5 and int(passed_id):
        return True
    else:
        print("The provided student ID is invalid")
        return False 

def validate_value(self, passed_value):
        if passed_value:
        return True
    else:
        print("You must provide a value")
        return False

college_records = []
my_validator = Validator()

while True:

    ind_type_valid = False 
    while ind_type_valid == False:
        ind_type = input("Are you a Student or Instructor? Type: 'S' or 'I' ")
        ind_type_valid = my_validator.validate_user_type(ind_type)

    ind_name_valid = False
    while ind_name_valid == False: 
        your_name = input("Enter your name: ")
        name_valid = my_validator.validate_name(your_name)

    ind_email_valid = False
    while ind_email_valid == False: 
        your_email = input("Enter your email: ")
        ind_email_valid = my_validator.validate_email(your_email)

    if ind_type.lower == "s":

    ind_id_valid = False
    while ind_id_valid == False: 
        your_id = input("Enter your Student ID: ")
        ind_id_valid = my_validator.validate_stud_id(your_id)

    ind_program_valid = False
    while ind_program_valid == False: 
        your_program = input("Enter your Program of Study: ")
        ind_program_valid = my_validator.validate_value(your_program)

    tmp_student = (your_name, your_email, your_id, your_program)
    college_records.append(tmp_student)

    else:
    ind_id_valid = False
    while ind_id_valid == False: 
        your_id = input("Enter your Instructor ID: ")
        ind_id_valid = my_validator.validate_instructor_id(your_id)

    ind_degree_valid = False
    while ind_degree_valid == False: 
        your_degree = input("Enter your Highest Degree: ")
        ind_degree_valid = my_validator.validate_value(your_degree)

    ind_institution_valid = False
    while ind_institution_valid == False: 
        your_institution = input("Enter the Last Instiution you Graduated from: ")
        ind_institution_valid = my_validator.validate_value(your_institution)

    tmp_instructor = Instructor{your_name, your_email, your_id, your_degree, your_institution}
    college_records.append(tmp_instructor)

    continue = input("Would you like to add another record (Y/N)? ")
    if continue.lower == "n":
        break

while college_records:
    print(college_records)