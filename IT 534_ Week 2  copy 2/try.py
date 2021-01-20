from Classes.VariableSort import VariableSort
from Functions.Function import Function

string = []
number = []
floating_point = []
'''
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
        flo_ok = x.Validate_floating_number(flo)
        if not flo_ok:
            flo = input("Please enter GPA again: ")
            flo_ok = x.Validate_floating_number(flo)
    return flo_ok
'''
while True:
    string_Variable = get_string()
    string.append(string_Variable)
    Integer_Variable = get_int()
    number.append(Integer_Variable)
    floating_Variable = get_float()
    floating_point.append(floating_Variable)

    response = input("Would you like to add another record (Y/N)? ")
    if response == "n":
        break
for x in string:
    print(f"List of Names:{string}")
    break
for y in number:
    print(f"List of Ages: {number}")
    break
for z in floating_Variable:
    print(f"List of GPA's{floating_point}")
    break



