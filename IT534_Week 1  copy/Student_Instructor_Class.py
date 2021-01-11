from Classes.Person import Person
from Classes.Instructor import Instructor
from Classes.Student import Student
from Classes.Validator import Validator
college_records = []
my_validator = Validator() 
"""Create a Instance of the Validator Class:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the input equals "S"
        * Create the instance of the functions inside Validator Class
        * Append instances to college Records
        Create for loop to display the information the user inputed
"""  
while True:
    ind_type = input("Are you a Student or Instructor? Type: 'S' or 'I' ")
    if ind_type == "S":
        your_id = input("Enter your Student ID: ")
        ind_id_valid = my_validator.validate_student_id(your_id)
        your_program = input("Enter your Program of Study: ")
        your_name = input("Enter your Name: ")
        name_valid = my_validator.validate_name(your_name)
        your_email = input("Enter your Email: ")
        ind_email_valid = my_validator.validate_email(your_email)
        tmp_student = Student(your_name, your_email, your_id, your_program)
        college_records.append(tmp_student)

    elif ind_type == "I":
        your_id = input("Enter your Instructor ID: ")
        ind_id_valid = my_validator.validate_instructor_id(your_id)
        your_name = input("Enter your Name:")
        name_valid = my_validator.validate_name(your_name)
        your_email = input("Enter your Email:")
        ind_email_valid = my_validator.validate_email(your_email)
        your_degree = input("Enter your Highest Degree: ")
        your_institution = input("Enter the Last Instiution you Graduated from: ")
        tmp_instructor = Instructor(your_name, your_email, your_id, your_degree, your_institution)
        college_records.append(tmp_instructor)
    

    response = input("Would you like to add another record (Y/N)? ")
    if response == "n":
        break
for x in college_records:
    print(x.displayInformation())



