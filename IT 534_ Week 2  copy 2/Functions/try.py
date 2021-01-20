from VariableSort import VariableSort
""" Create a three variable with list as values"""

def get_string():
    """ Create the a method to create a string variable to vaildate""" 
    string = input("Enter Name:")

    string_ok = False

    while not string_ok:
        """ Create an instance to sort the variables"""
        x = VariableSort("James", 32, 5.4)

        string_ok = x.Validate_string(string)

        if not string_ok:
            string = input("Please enter name again: ")
            string_ok = x.Validate_string(string)
    return string_ok

def get_int():
    """ Create a method to create a interger variable to vaildate""" 
    number = input("Enter Age:")

    number_ok = False 
    
    while not number_ok:
        """ Create an instance to sort the variables"""
        x = VariableSort("Rick",2,3.4)
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
        x = VariableSort("Kame",23,3.2)
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
    print(f"List of String Values:{string_Variable}")
    break
for y in Integer_Variable:
    print(f"List of Integer Values: {Integer_Variable}")
    break
for z in floating_Variable:
    print(f"List of Float Values: {floating_Variable}")
    break



