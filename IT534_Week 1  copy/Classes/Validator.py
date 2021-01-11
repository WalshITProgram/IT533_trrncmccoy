class Validator():
    """Create a Class Validator:
List of functions inside a Class
1. Inherit the constructor from the Parent Class.
Create Validate_Name function:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the length is equal to zero
        * Repeat until valid input 
        * Create for loop to iterate through the passed_name
        * if it does not contain invalid characters 
        return passed_name
    """
    def validate_name(self, passed_name):
        invalid_chars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ':', ';', ']', '[', '}', '{', '/', '\\']
        while True:
            if (len(passed_name) == 0):
                continue
            bad_char = False
            for character in passed_name:
                if not invalid_chars and not character.isalpha():
                    bad_char = True
                    break
                if bad_char == False:
                    return passed_name 

    """Create Validate_Email function:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the length is equal to zero
        * Repeat until valid input 
        * Create for loop to iterate through the passed_email
        * if it does not contain invalid characters 
        return passed_email 
    """   
    def validate_email(self, passed_email):
        Email_valid_char = ['@', '.']
        invalid_chars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ':', ';', ']', '[', '}', '{', '\\']
        while True:
            if len(passed_email) == 0:
                continue
            bad_char = False
            for character in passed_email:
                if character.isalnum() and character not in Email_valid_char:
                     return passed_email
            else:
                print("Your email has bad characters in it")
            break
    """Create Validate_Student_ID function:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the length of the id is less 7
        * Repeat until valid input 
        * Change the data type to int
        return passed_id 
    """   
    def validate_student_id(self, passed_id):
        if len(passed_id) <= 7:
            try:
                int(passed_id)
                return passed_id
            except:
                print("The provided student ID is invalid")
    """Create Validate_Student_ID function:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the length of the id is less 7
        * Repeat until valid input 
        * Change the data type to int
        return passed_id 
    """     
    def validate_instructor_id(self, passed_id):
        if len(passed_id) <= 5: 
            try:
                if int(passed_id):
                    return passed_id
            except:
                print("The provided instructor ID is invalid")
"""Create Validate_Instructor_ID function:
1. Create a While Loop:
    * Implement a Condition Statement:
        * If the length of the id is less 5
        * Repeat until valid input 
        * Change the data type to int
        return passed_id 
"""          


