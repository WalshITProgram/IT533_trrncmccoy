class Validator():
    def validate_name(self, passed_name):
        invalid_chars = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ':', ';', ']', '[', '}', '{', '/', '\\']
        while True:

            if len(passed_name) == 0:
                bad_char = False
                continue

            for character in passed_name:
                if not character.isalpha and invalid_chars:
                    bad_char = True
                    break
                if bad_char == False:
                    return passed_name 

    
    def validate_email(self, passed_email):
        invalid_chars = ['!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ':', ';', ']', '[', '}', '{', '\\']
        while True:
            if len(passed_email) == 0:
                bad_char = False
                for character in passed_email:
                    if not character.isalnum() and invalid_chars:
                        bad_char = True 
                        break
                    if bad_char == False:
                        return 


            else:
                print("Your email has bad characters in it")
      

    def validate_user_type(self, passed_type):
        if passed_type == "S " or passed_type == "I":
            try:
                passed_type.isalpha
            except:
                print("The provided user type is invalid")
            

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


