from VariableSort import VariableSort
def get_string():
    string = input("Enter Name:")

    string_ok = False

    while not string_ok:
        x = VariableSort("", "", "")

        string_ok = x.Validate_string(string)

        if not string_ok:
            string = input("Please enter name again: ")
            string_ok = x.Validate_string(string)
    return string_ok

def get_int():
    number = input("Enter Age:")

    number_ok = False 
    
    while not number_ok:
        x = VariableSort("","","")
        number_ok = x.Validate_integer(number)
        if not number_ok:
            number = input("Please enter age again: ")
            number_ok = x.Validate_integer(number)
    return number_ok

def get_float():
    flo = input("Enter GPA:") 

    flo_ok = False

    while not flo_ok:
        x = VariableSort("","","")
        flo_ok = x.Validate_integer(flo)
        if not flo_ok:
            flo = input("Please enter GPA again: ")
            flo_ok = x.Validate_floating_number(number)
    return flo_ok
