Employees = [1121, "Jackie Grainger", 22.22, 1122, 
"Jignesh Thrakkar", 22.25, 1127, "Dion Green", 28.75, 
False, 24.32, 1132, "Jacob Gerber", "Sarah Sander", 
23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 
1152, "David Toma", 22.65, 23.75, 1157, "David Toma", 
22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 
1121, 22,22, False, 22.65, 1152, "David Toma"]
Employees1 = list(filter(bool, Employees))


Id = [{"Customer ID" : 1121, "Name" : "Jackie Grainger", "Hourly Wage" : 22.22}, 
{"Customer ID" : 1122, "Name" : "Jignesh Thrakkar", "Hourly Wage" : 22.25}, 
{"Customer ID" : 1127, "Name" : "Dion Green", "Hourly Wage" : 28.75},
{"Customer ID" : 1132, "Name" : "Jacob Gerber", "Hourly Wage" : 24.32},
{"Customer ID" : 1137, "Name" : "Sarah Sander", "Hourly Wage" : 23.45},
{"Customer ID" : 1138, "Name" : "Brandon Heck", "Hourly Wage": 25.84},
{"Customer ID" : 1152, "Name" : "David Toma", "Hourly Wage" : 22.65},
{"Customer ID" : 1157, "Name" : "Charles King", "Hourly Wage" : 23.75}]

#print(sorted(Id, key = lambda i: (i["Hourly Wage"], i["Customer ID"], i["Name"])))


    #print(K)

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
#print(datastore["Employees"]["Employee"])

underpaid_salaries = []
company_raises = []

space = datastore["Employees"]["Employee"]
for i in space:
    if i.get('Hourly Wage') == 22.22: 
        i['Total Hourly Wage'] = round(1.3 * 22.22)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[0])
            if i.get('Hourly Wage') == 22.22:
               i['Hourly Wage'] = 22.22 * 1.05
               company_raises.append(space[0])
           
                  

    elif i.get('Hourly Wage') == 25.25: 
        i['Total Hourly Wage'] = round(1.3 * 25.25)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[1])
    if i.get('Hourly Wage') == 25.25:
       i['Hourly Wage'] = 25.25 * 1.04
       company_raises.append(space[1])
        
    elif i.get('Hourly Wage') == 28.75:
        i['Total Hourly Wage'] = round(1.3 * 28.75)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[2])
    if i.get('Hourly Wage') == 28.75:
       i['Hourly Wage'] = 28.75 * 1.03
       company_raises.append([space[2]])

    elif i.get('Hourly Wage') == 24.32:
        i['Total Hourly Wage'] = round(1.3 * 24.32)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[3])
    if i.get('Hourly Wage') == 24.32:
       i['Hourly Wage'] = 24.32 * 1.05
       company_raises.append([space[3]])

    elif i.get('Hourly Wage') == 23.45:
        i['Total Hourly Wage'] = round(1.03 * 23.45)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[4])
    if i.get('Hourly Wage') == 23.45:
       i['Hourly Wage'] = 23.45 * 1.05
       company_raises.append([space[4]])

    elif i.get('Hourly Wage') == 25.84:
        i['Total Hourly Wage'] = round(1.3 * 25.84)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[5])
    if i.get('Hourly Wage') == 25.84:
       i['Hourly Wage'] = 25.84 * 1.04
       company_raises.append(space[5])

    elif i.get('Hourly Wage') == 22.65:
        i['Total Hourly Wage'] = round(1.3 * 22.65)
        if i['Total Hourly Wage'] < 30.65:
         underpaid_salaries.append(space[6])
    if i.get('Hourly Wage') == 22.65:
       i['Hourly Wage'] = 22.65 * 1.05
       company_raises.append(space[6])

    elif i.get('Hourly Wage') == 23.75:
        i['Total Hourly Wage'] = round(1.3 * 23.75)
        if i['Total Hourly Wage'] < 30.65:
            underpaid_salaries.append(space[7])
    if i.get('Hourly Wage') == 23.75:
       i['Hourly Wage'] = 23.75 * 1.05
       company_raises.append(space[7])
    print(i)
print(underpaid_salaries)


print(company_raises)

