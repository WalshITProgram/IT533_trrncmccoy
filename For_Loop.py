# Create a program that gathers information 
programs = True 
while programs:
    Employee_ID = input("Enter Your Employee ID:")
    Employee_Name = input("Enter Your Name:")
    Employee_Email = input("Enter Email:")
    try: 
        int(Employee_ID)
        str(Employee_Name)
        str(Employee_Email)
    except:
        print("You entered an invalid ! Please try again.")

    Repeat = input('Would you like to add another record? (Y,N)')
    if Repeat == 'N':
        programs = False
    
