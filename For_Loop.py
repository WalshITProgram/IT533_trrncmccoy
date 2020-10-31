# Create a program that gathers information 
Email_Keys = [ '!','\'', "\"", '#', '$', '%', '^', '&', '*', '(', ')',  '=', '+' , '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\' ]
Address_Keys = ['!', '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
valid_name_chars = [" ",'\'','-']
list_of_employees = []
while True:
   employee_dict = {}
   while True:
      Employee_ID = input("Enter Your Employee ID:")
      
      if (len(Employee_ID) <= 7):
         try:
            int(Employee_ID)
            employee_dict['ID'] = Employee_ID
            break
         except: 
            print("You entered an invalid ID number! Please try again.")
   
   while True:
      entered_name = input("Enter your name:")
      if len(entered_name) == 0:
         continue
      bad_char_hit = False
      for letter in entered_name:
         if letter not in valid_name_chars and not letter.isalpha():
            bad_char_hit = True
            
      if bad_char_hit == False:
         employee_dict['Name'] = entered_name
         break
   while True: 
      Employee_Email = input("Enter Email:")
      if len(Employee_Email) == 0:
         continue
      bad_char_hit = False
      for char in Employee_Email:
         if char not in Email_Keys and not char.isalnum():
            bad_char_hit = True 

      if bad_char_hit == False:
         employee_dict['Email'] = Employee_Email
         break
   while True:
      Employee_Address = input("Enter Address:")
      bad_char_hit = False
      for char in Employee_Address:
         if char not in Employee_Address and not char.isalnum():
            bad_char_hit = True 
      if bad_char_hit == False:
         employee_dict['Address'] = Employee_Address
         break
   while True:
      Employee_Salary = input("Enter Salary Between 18 & 27:")
      try:
         if float(Employee_Salary) >= 18.00 and float(Employee_Salary) <= 27.00:
            employee_dict['Salary'] = float(Employee_Salary)
            break
      except: 
         print("You entered an invalid salary! Please try again.")
   list_of_employees.append(employee_dict)
   Repeat = input('Would you like to add another record? (Y,N)')
   if Repeat == 'N':
      break
for index, employee in enumerate(list_of_employees):
   list_of_employees[index]["Name"] = list_of_employees[index]["Name"] + "IT Department"
   list_of_employees[index]["Total Hourly Salary"] = list_of_employees[index]["Salary"] * 1.3
for employee in list_of_employees:
   print(employee)


    
