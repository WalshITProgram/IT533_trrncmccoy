# Create a program that gathers information 
programs = True 
ID = []
Names = []
Email = []
Salary = []
Incorrect_Keys = ['!', '@', '$', '%', '^', '&', '*',' _',  '=', '+', '<', '>',  '?', ';', ':', '[ ]', '{ }']
while programs: 
      Employee_ID = (input("Enter Your Employee ID:")) 
      if len(Employee_ID) < 7:
         ID.append(Employee_ID)
      Employee_Name = input("Enter Your Full Name:")
      if str(Employee_Name).isalpha():
         Names.append(Employee_Name)
      Employee_Email = input("Enter Email:")
      if str(Employee_Email).isalnum(): 
         Email.append(Employee_Email)
      Employee_Salary = int(input("Enter Salary Between 18 & 27:"))
      if Employee_Salary >= 18 and Employee_Salary <= 27: 
         Salary.append(float(Employee_Salary))          
try:
      int(Employee_ID)
      str(Employee_Name)
      str(Employee_Email)
      float(Employee_Salary)
except:
      print("You entered an invalid ! Please try again.")
Repeat = input('Would you like to add another record? (Y,N)')
if Repeat == 'N':
      programs = False
      if Repeat =='Y':
         programs = True
print(ID)
print(Names)
print(Email)
print(Salary)

list_of_employees = []

for index, Name in enumerate(Names):
   employee_dict = {'ID': ID[index], 'Names': Names[index] + " " +  str('IT Department'), 'Email':Email[index], 'Salary': Salary[index], 'Total Salary': Salary[index] * 1.3 }
   list_of_employees.append(employee_dict)
   print(list_of_employees)


    
