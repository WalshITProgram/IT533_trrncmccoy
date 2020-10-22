Employees = [1121, "Jackie Grainger", 22.22, 1122, 
"Jignesh Thrakkar", 22.25, 1127, "Dion Green", 28.75, 
False, 24.32, 1132, "Jacob Gerber", "Sarah Sander", 
23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 
1152, "David Toma", 22.65, 23.75, 1157, "David Toma", 
22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 
1121, 22,22, False, 22.65, 1152, "David Toma"]

Id = [{"Customer ID" : 1121, "Name" : "Jackie Grainger", "Hourly Wage" : 22.22}, 
{"Customer ID" : 1122, "Name" : "Jignesh Thrakkar", "Hourly Wage" : 22.25}, 
{"Customer ID" : 1127, "Name" : "Dion Green", "Hourly Wage" : 28.75},
{"Customer ID" : 1132, "Name" : "Jacob Gerber", "Hourly Wage" : 24.32},
{"Customer ID" : 1137, "Name" : "Sarah Sander", "Hourly Wage" : 23.45},
{"Customer ID" : 1138, "Name" : "Brandon Heck", "Hourly Wage": 25.84},
{"Customer ID" : 1152, "Name" : "David Toma", "Hourly Wage" : 22.65},
{"Customer ID" : 1157, "Name" : "Charles King", "Hourly Wage" : 23.75}]

#print(sorted(Id, key = lambda i: (i["Hourly Wage"], i["Customer ID"], i["Name"])))


for i in Id:
    K = (f"Employee ID: {i['Customer ID']}  Name: {i.get('Name')}  Hourly Wage: {i.get('Hourly Wage')}")
    print(K)

datastore = {"Employees":{
    "Employee": [
        {"Customer ID" : 1121,
         "Name" : "Jackie Grainger", 
         "Hourly Wage" : 22.22}, 
        
        {"Customer ID" : 1122, 
        "Name" : "Jignesh Thrakkar", 
        "Hourly Wage" : 25.25}, 
        
        {"Customer ID" : 1127, 
        "Name" : "Dion Green", 
        "Hourly Wage" : 28.75},
        
        {"Customer ID" : 1132, 
        "Name" : "Jacob Gerber", 
        "Hourly Wage" : 24.32},
        
        {"Customer ID" : 1137, 
        "Name" : "Sarah Sander", 
        "Hourly Wage" : 23.45},
        
        {"Customer ID" : 1138,
         "Name" : "Brandon Heck", 
         "Hourly Wage": 25.84},
       
        {"Customer ID" : 1152,
         "Name" : "David Toma", 
         "Hourly Wage" : 22.65},
        
        {"Customer ID" : 1157,
         "Name" : "Charles King", 
         "Hourly Wage" : 23.75}

    ]
} }
print(datastore["Employees"]["Employee"])

underpaid_salaries = []
space = datastore["Employees"]["Employee"]
for i in space:
    if i.get('Hourly Wage') == 22.22: 
        i['Total Hourly Wage'] = round(1.3 * 22.22)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[0])
    elif i.get('Hourly Wage') == 25.25: 
        i['Total Hourly Wage'] = round(1.3 * 25.25)

    elif i.get('Hourly Wage') == 28.75:
        i['Total Hourly Wage'] = round(1.3 * 28.75)
    elif i.get('Hourly Wage') == 24.32:
        i['Total Hourly Wage'] = round(1.3 * 24.32)
    elif i.get('Hourly Wage') == 23.45:
        i['Total Hourly Wage'] = round(1.3 * 23.45)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[4])
    elif i.get('Hourly Wage') == 25.84:
        i['Total Hourly Wage'] = round(1.3 * 25.84)
    elif i.get('Hourly Wage') == 22.65:
        i['Total Hourly Wage'] = round(1.3 * 22.65)
        if i['Total Hourly Wage'] < 30.65:
         underpaid_salaries.append(space[6])
    elif i.get('Hourly Wage') == 23.75:
        i['Total Hourly Wage'] = round(1.3 * 23.75)
    print(i)
print(underpaid_salaries)

  
    







