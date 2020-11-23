import json
# Create a program that gathers information 
# List of chars that cannot be included into the employees email 
Email_Keys = [ '!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
Address_Keys = ['!', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
# Valid characters for employee name
valid_name_chars = [" ",'\'','-']
# The list for dictionary items  
list_of_employees = []
def employee(employee_dict): 
	while True:
		Employee_ID = input("Enter Your Employee ID:")
		# If less then 7 and not a int must repeat input
		if (len(Employee_ID) <= 7):
			# If valid add it to employee dict [ID]
			try:
				int(Employee_ID)
				employee_dict['ID'] = Employee_ID
				break
			except: 
				print("You entered an invalid ID number! Please try again.")
def employee_name(employee_dict):
	while True:
		entered_name = input("Enter your Name:")
		if len(entered_name) == 0:
			continue
		bad_char_hit = False
# Create a for loop to iterate through chars entered 
		for letter in entered_name:
	# Set condition statement to test if the input has letters and valid chars
			if letter not in valid_name_chars and not letter.isalpha():
				bad_char_hit = True
# if returned false add employee name      
		if bad_char_hit == False:
			employee_dict['Name'] = entered_name
			break
      # If emails does not contain emails keys/num/alpha repeats until correct
# Create a while loop to repeat users input
def employee_info(employee_dict, typeinput):
	while True: 
		Employee_input = input(typeinput)
		if len(Employee_input) == 0:
			continue
		bad_char_hit = False
		if typeinput == "Email":
			for char in Employee_input:
				if char not in Email_Keys and not char.isalnum():
					bad_char_hit = True 
					
		if typeinput == "Address":
			for char in Employee_input:
				if char not in Address_Keys and not char.isalnum():
					bad_char_hit = True		

		if bad_char_hit == False:
			employee_dict[typeinput] = Employee_input
			break
      # Same sequence of events from line 40-51

def employee_salary(employee_dict):
	while True:
		Employee_Salary = input("Enter Salary Between 18 & 27:")
		try:
			if float(Employee_Salary) >= 18.00 and float(Employee_Salary) <= 27.00:
				employee_dict['Salary'] = float(Employee_Salary)
				break
		except: 
			print("You entered an invalid salary! Please try again.")

while True:
	employee_dict = {}
   #  employee name
	employee(employee_dict)
	employee_name(employee_dict)
	employee_info(employee_dict, "Address:")
	employee_info(employee_dict,"Email:")
	
	employee_salary(employee_dict)
	list_of_employees.append(employee_dict)
	Repeat = input('Would you like to add another record? (Y,N)')
	if Repeat == 'N':
		break
# Create a for loop to iterate through the list of employees 
'''
for index, employee in enumerate(list_of_employees):
   # Add IT department 
   list_of_employees[index]["Name"] = list_of_employees[index]["Name"] + " IT Department"
   # Create key called Total Hourly Salary
   list_of_employees[index]["Total Hourly Salary"] = list_of_employees[index]["Salary"] * 1.3
for employee in list_of_employees:
   print(employee)
'''
def json_file(list_of_employees):
	for index, employee in enumerate(list_of_employees):
   # Add IT department 
   		list_of_employees[index]["Name"] = list_of_employees[index]["Name"] + " IT Department"
   # Create key called Total Hourly Salary
   		list_of_employees[index]["Total Hourly Salary"] = list_of_employees[index]["Salary"] * 1.3
	s = json.dumps(list_of_employees)
# Write to the JSON file by dumping the dictionary
	json.dump(list_of_employees, fp=open("Employee_List.json", 'w'), indent = 4)
	json_file = open("Employee_List.json")
	print(open("Employee_List.json").read())
	json_file.close()	
json_file(list_of_employees)
	 