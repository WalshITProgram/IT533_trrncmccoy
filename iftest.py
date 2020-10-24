# List of Employee Information(Employee ID, Name, & Hourly Wage)
Employees = [1121, "Jackie Grainger", 22.22, 1122, 
"Jignesh Thrakkar", 22.25, 1127, "Dion Green", 28.75, 
False, 24.32, 1132, "Jacob Gerber", "Sarah Sander", 
23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 
1152, "David Toma", 22.65, 23.75, 1157, "David Toma", 
22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 
1121, 22,22, False, 22.65, 1152, "David Toma"]
# Create a list that filters out redundant data
Employees1 = list(filter(bool, Employees))
# Create a list with dictionary items
Id = [{"Customer ID" : 1121, "Name" : "Jackie Grainger", "Hourly Wage" : 22.22}, 
{"Customer ID" : 1122, "Name" : "Jignesh Thrakkar", "Hourly Wage" : 22.25}, 
{"Customer ID" : 1127, "Name" : "Dion Green", "Hourly Wage" : 28.75},
{"Customer ID" : 1132, "Name" : "Jacob Gerber", "Hourly Wage" : 24.32},
{"Customer ID" : 1137, "Name" : "Sarah Sander", "Hourly Wage" : 23.45},
{"Customer ID" : 1138, "Name" : "Brandon Heck", "Hourly Wage": 25.84},
{"Customer ID" : 1152, "Name" : "David Toma", "Hourly Wage" : 22.65},
{"Customer ID" : 1157, "Name" : "Charles King", "Hourly Wage" : 23.75}]
# Use Lambda Tool to sort the items by Hourly Wage
#print(sorted(Id, key = lambda i: (i["Hourly Wage"], i["Customer ID"], i["Name"])))
# Create a the dictionary list in a database format
datastore = {"Employees":{
    "Employee": [
        {"Employee ID" : 1121,
         "Name" : "Jackie Grainger", 
         "Hourly Wage" : 22.22}, 
        
        {"Employee ID" : 1122, 
        "Name" : "Jignesh Thrakkar", 
        "Hourly Wage" : 25.25}, 
        
        {"Employee ID" : 1127, 
        "Name" : "Dion Green", 
        "Hourly Wage" : 28.75},
        
        {"Employee ID" : 1132, 
        "Name" : "Jacob Gerber", 
        "Hourly Wage" : 24.32},
        
        {"Employee ID" : 1137, 
        "Name" : "Sarah Sander", 
        "Hourly Wage" : 23.45},
        
        {"Employee ID" : 1138,
         "Name" : "Brandon Heck", 
         "Hourly Wage": 25.84},
       
        {"Employee ID" : 1152,
         "Name" : "David Toma", 
         "Hourly Wage" : 22.65},
        
        {"Employee ID" : 1157,
         "Name" : "Charles King", 
         "Hourly Wage" : 23.75}

    ]
} }
#print(datastore["Employees"]["Employee"])
# Create a two empty list 
underpaid_salaries = []
company_raises = []
# Create a variable storing the keys
# In order to address a specific portion of the datastore 
space = datastore["Employees"]["Employee"]
# Create a Loop to iterate through the key items in space
for i in space:
    # Create a if statement that multiplies hourly wage times 1.3
    if i.get('Hourly Wage') == 22.22: 
        i['Total Hourly Wage'] = round(1.3 * 22.22)
        # Append the result of Total Hour Wage to underpaid if between 28.15 and 30.65
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[0])
            # Append the result of Hourly Wage to Company raise 
            # If hourly rate is between 22 and 24 apply 5%
        if i.get('Hourly Wage') == 22.22:
           i['Hourly Wage'] = round(22.22 * 1.05)
           company_raises.append(space[0])
           
                  

    elif i.get('Hourly Wage') == 25.25: 
        i['Total Hourly Wage'] = round(1.3 * 25.25)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[1])
    # If hourly rate is between 24 and 25 apply 4%
    if i.get('Hourly Wage') == 25.25:
       i['Hourly Wage'] = round(25.25 * 1.04)
       company_raises.append(space[1])
        
    elif i.get('Hourly Wage') == 28.75:
        i['Total Hourly Wage'] = round(1.3 * 28.75)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[2])
    # If hourly rate is between 26 and 28 apply 3%
    if i.get('Hourly Wage') == 28.75:
       i['Hourly Wage'] = round(28.75 * 1.03)
       company_raises.append([space[2]])

    elif i.get('Hourly Wage') == 24.32:
        i['Total Hourly Wage'] = round(1.3 * 24.32)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[3])
    # If hourly rate is between 22 and 24 apply 5%
    if i.get('Hourly Wage') == 24.32:
       i['Hourly Wage'] = round(24.32 * 1.05)
       company_raises.append([space[3]])

    elif i.get('Hourly Wage') == 23.45:
        i['Total Hourly Wage'] = round(1.03 * 23.45)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[4])
    # If hourly rate is between 22 and 24 apply 5%
    if i.get('Hourly Wage') == 23.45:
       i['Hourly Wage'] = round(23.45 * 1.05)
       company_raises.append([space[4]])

    elif i.get('Hourly Wage') == 25.84:
        i['Total Hourly Wage'] = round(1.3 * 25.84)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[5])
    # If hourly rate is between 22 and 24 apply 4%
    if i.get('Hourly Wage') == 25.84:
       i['Hourly Wage'] = round(25.84 * 1.04)
       company_raises.append(space[5])

    elif i.get('Hourly Wage') == 22.65:
        i['Total Hourly Wage'] = round(1.3 * 22.65)
        if i['Total Hourly Wage'] < 30.65:
         underpaid_salaries.append(space[6])
    # If hourly rate is between 22 and 24 apply 5%
    if i.get('Hourly Wage') == 22.65:
       i['Hourly Wage'] = round(22.65 * 1.05)
       company_raises.append(space[6])

    elif i.get('Hourly Wage') == 23.75:
        i['Total Hourly Wage'] = round(1.3 * 23.75)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[7])
    # If hourly rate is between 22 and 24 apply 5%
    if i.get('Hourly Wage') == 23.75:
       i['Hourly Wage'] = round(23.75 * 1.05)
       company_raises.append(space[7])
    print(f"Employee List: {i}")

for x in underpaid_salaries:
    K = (f"Employee ID: {x['Employee ID']} Name: {x.get('Name')} Hourly Wage: {x.get('Hourly Wage')}")
    print(f"Underpaid Employees: {x}")

for a in company_raises:
     K = (f"Employee ID: {x['Employee ID']} Name: {x.get('Name')} Hourly Wage: {x.get('Hourly Wage')}")
     print(f"Employee Raises:{a}")



