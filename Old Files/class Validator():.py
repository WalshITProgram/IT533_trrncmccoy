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
