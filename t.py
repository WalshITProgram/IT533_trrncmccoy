for i in Id:
    K = (f"Employee ID: {i['Customer ID']}  Name: {i.get('Name')}  Hourly Wage: {i.get('Hourly Wage')}")
    if i.get('Hourly Wage') == 22.22:
       i['Hourly Wage'] = 1.05 * 22.22
       company_raises.append(space[0])