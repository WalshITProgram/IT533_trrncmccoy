from Classes.Person import Person
from Classes.Instructor import Instructor
from Classes.Student import Student
from Classes.Validator import Validator
college_records = []
my_validator = Validator() 

while True:
    ind_type = input("Are you a Student or Instructor? Type: 'S' or 'I' ")
    ind_type_valid = my_validator.validate_user_type(ind_type)

    your_name = input("Enter your name: ")
    name_valid = my_validator.validate_name(your_name)

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

        tmp_instructor = Instructor(your_name, your_email, your_id, your_degree, your_institution)
        college_records.append(tmp_instructor)

    response = input("Would you like to add another record (Y/N)? ")
    if response.lower == "n":
        break

while college_records:
    print(college_records)