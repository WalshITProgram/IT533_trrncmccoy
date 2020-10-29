programs = True
Employee_ID = input("Enter Your Employee ID:")
while programs:
   try:
      
      if len(int(Employee_ID)) <= 7:
         ID.append(Employee_ID)
   except:
      print("You entered an invalid ! Please try again.")

   Repeat = input('Would you like to add another record? (Y,N)')
   if Repeat == 'N':
      programs = False
      if Repeat =='Y':
          programs = True