from Classes.VariableSort import VariableSort
""" Create a three variable with list as values"""
def get_string():
    """ Create the a method to create a string variable to vaildate""" 
    string = input("Enter Name:")

    string_ok = False

    while not string_ok:
        """ Create an instance to sort the variables"""
        x = VariableSort("", "", "")

        x.Validate_string(string)

        if not string_ok:
            string = input("Please enter name again: ")
            x.Validate_string(string)
    return x.Validate_string

def get_int():
    """ Create a method to create a interger variable to vaildate""" 
    number = input("Enter Age:")

    number_ok = False 
    
    while not number_ok:
        """ Create an instance to sort the variables"""
        x = VariableSort("","","")
        number_ok = x.Validate_integer(number)
        if not number_ok:
            number = input("Please enter age again: ")
            number_ok = x.Validate_integer(number)
    return number_ok

def get_float():
    """ Create a method to create a floating variable to vaildate""" 
    flo = input("Enter GPA:") 

    flo_ok = False

    while not flo_ok:
        """ Create an instance to sort the variables"""
        x = VariableSort("","","")
        flo_ok = x.Validate_floating_number(flo)
        if not flo_ok:
            flo = input("Please enter GPA again: ")
            flo_ok = x.Validate_floating_number(flo)
    return flo_ok

while True:
    string_Variable = get_string()
    Integer_Variable = get_int()
    floating_Variable = get_float()
 

    response = input("Would you like to add another record (Y/N)? ")
    if response == "n":
        break
for x in string_Variable:
    print(f"List of Names:{string_Variable}")
    break
for y in Integer_Variable:
    print(f"List of Ages: {Integer_Variable}")
    break
for z in floating_Variable:
    print(f"List of GPA's:{floating_Variable}")
    break



