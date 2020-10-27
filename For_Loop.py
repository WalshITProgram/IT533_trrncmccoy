# Create a program that gathers information 
programs = True 
ID = []
Names = []
Email = []
while programs:
   Employee_ID = input("Enter Your Employee ID:")
   if len(Employee_ID) <= 7:
       ID.append(Employee_ID)
   Employee_Name = input("Enter Your Full Name:")
   if Employee_Name.isspace():
      Names.append(Employee_Name) 
   Employee_Email = input("Enter Email:")
   if Employee_Email.isalpha(): 
      Email.append(Employee_Email)          
   try: 
      int(Employee_ID)
      str(Employee_Name)
      str(Employee_Email)
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

    
