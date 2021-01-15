from Classes.VariableSort import VariableSort
    
jas = input("Enter word:")
num = input("Enter number:")
flo = input("Enter decimal:")
x = VariableSort(jas, num, flo)
x.Validate_string(jas)
x.Validate_integer(num)
x.Validate_floating_number(flo)





