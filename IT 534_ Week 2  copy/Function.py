from Classes.VariableSort import VariableSort
def get_string():
    string = input("Enter Name:")

    string_ok = False

    while not string_ok:
        x = VariableSort("", "", "")

        string_ok = x.Validate_string(string)

        if not string_ok:
            string = input("Please enter name again!")
            string_ok = x.Validate_string(string)
    return string_ok

print(get_string())