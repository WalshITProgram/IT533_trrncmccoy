Employees = [1121, "Jackie Grainger", 22.22, 1122, 
"Jignesh Thrakkar", 22.25, 1127, "Dion Green", 28.75, 
False, 24.32, 1132, "Jacob Gerber", "Sarah Sander", 
23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 
1152, "David Toma", 22.65, 23.75, 1157, "David Toma", 
22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 
1121, 22,22, False, 22.65, 1152, "David Toma"]
names = []
pay = []
ids = []

for value in Employees:
    if type(value) == str:
        names.append(value)
    if type(value) == float:
        pay.append(value)
    if type(value) == int:
        ids.append(value)

print(f"Employee Names: {names}")
print(f"Salary: {pay}")
print(f"IDs: {ids}")

names.pop(10) 
names.pop(9) 
pay.pop(10) 
pay.pop(9) 
ids.pop(10) 
ids.pop(9)



list_of_employees = []

for index, name in enumerate(names):
    employee_dict = {'Name': names[index], 'Salary': pay[index], 'ID': ids[index], 'Total-Hourly-Wage': pay[index] * 1.3}
    list_of_employees.append(employee_dict)
    
print(f"List of Employees:{list_of_employees}")

underpaid_salaries = []
company_raises = [ ]

for employee in list_of_employees:
    if employee['Total-Hourly-Wage'] >= 28.15 and employee['Total-Hourly-Wage'] <= 30.65:
        underpaid_salaries.append(employee)
        

           
          
for employee in list_of_employees:
    if employee['Salary'] >= 22 and employee['Salary'] < 24:
        employee['Salary'] = employee['Salary'] * 1.05
    elif employee['Salary'] >= 24 and employee['Salary'] < 26:
         employee['Salary'] = employee['Salary'] * 1.04
    elif employee['Salary'] >= 26 and employee['Salary'] < 28:
         employee['Salary'] = employee['Salary'] * 1.03
    else:
        employee['Salary'] = employee['Salary'] * 1.02
    
    company_raises.append(employee)
    
print(f"Underpaid Salaries: {underpaid_salaries}")
print(f"Company Raise: {company_raises}")
 
        



