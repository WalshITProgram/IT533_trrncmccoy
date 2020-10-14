# Pick 5 different assignment statement forms 

# Basic Assignments 
Workout_Plan = "HIIT" 

# Tuple Assignment
plan_a, plan_b, plan_c = "Cardio", "WeightLifting", "Crossfit" 

# WeightLifting Variables 
Bench_Press = " Bench Press: 5 sets X 5 reps "
Dumbbell = " Dumbbell Press: 10 sets x 10 reps"
Incline_Bench_Press = " Incline Bench Press: 5 set x 15 reps"
Dumbbell_Incline = " Dumbbell Incline: 5 set x 25 reps"
Dumbbell_Flat_Bench = " Dumbbell Flat Bench: 5 set x 20 reps"

# List Assignments
Core = [
    Workout_1, Workout_2,
    Workout_3,Workout_4, 
    Workout_5] = [
        Bench_Press, Incline_Bench_Press, 
        Dumbbell_Incline, Dumbbell_Flat_Bench, 
        Dumbbell ] 

# Cardio Variables
# List of Workouts
Cardio_Routine = [
    " 20 Min Run", 
    " 30 Min Shadow Boxing", 
    " 20 Burprees"] 

# Crossfit Variables & Dictionary 
Pullups = " 10 Wide Grip Pulls Ups"
Pushups = " 50 Push Ups"
Sqauts = " 50 Sqauts"
Burpees = " 50 Burpees"

# Hanging Indents 
Crossfit = {
            Pullups, Pushups, 
            Sqauts, Burpees}

# Sequence Assignment
a, b, c, d = Workout_Plan  

# Multiple Target Assignment 
RBX = RXP = "Strength Testing"  

while True:
 print(f"Welcome to {Workout_Plan}!")
 print(f"Please select your plan: {plan_a}, {plan_b}, {plan_c}")
 user = input("Select Workout Plan:")

 if (user == plan_a or 
     user == "cardio"): 
     print(f"You have selected: {plan_a}")
     for i in Cardio_Routine: print(f"Cardio Routine: {i}") 
     break
 
 if (user == plan_b or 
    user == "weightlifting"): 
     print(f"You have selected: {plan_b}")
     for t in Core: print(f"Chest Routine:{t}")
     break

 if (user == plan_c or
     user == "crossfit"): 
     print(f"You have selected: {plan_c}")
     for x in Crossfit: print(f"Crossfit Routine:{x}")
     break
 
# Weights Advanced Sequence Assignment Patterns
Weights = '0123456789'
set1, set2, set3, set4, set5, set6, set7, set8, set9, set10 = Weights
Weight = set2 + set4 + set5
#print(Weight)

# Calculating the BMR = 10 x Weight(kg) x Height(cm) - 5 x age(years) + 5
# Weight Variables Converting lbs to kg 
# BMR is an estimate of the amount of energy (calories) that your body expends when completely at rest. 
lbs = int(input("Enter Your Weight:"))

# Kilograms to pounds formula
kg = lbs / 2.2046226218

# Height Variables convert inches into cm
Height = "Please Enter Your Height in Feet & Inches:"
feet = int(input("Enter Your Height in Feet:"))
inches = int(input("Enter the Inches:"))
cm = feet * 12
cm1 = cm + inches
cm2 = cm1 * 2.54
import math

# Age Variables 
age = int(input("Enter Your Age:"))

# Gender Variable 
Gender = input("Are you a Male or Female:")
Male = "Male"
Female = "Female"

# BMR Variable and match operators with operands 
BMR = (10 
       * kg 
       + 6.25 
       * cm2 
       - 5 
       * age 
       + 5)
BMR1 = (10 
        * kg 
        + 6.25
        * cm2 
        - 5 
        * age 
        - 161)

# Calculate Total Daily Caloric Needs 
Studying = 1.30
Walking = 1.55
Jogging = 1.65
BodyBuilding = 1.80
Heavy_WeightLifting = 2.00
TDCN = {Studying, Walking, Jogging, BodyBuilding, Heavy_WeightLifting}
Activity = input("Select Daily Activity: Studying, Walking, Jogging, BodyBuilding, Heavy WeightLifting\n")

# Mens Daliy Caloric Variables 
Mtotal = math.floor(BMR) * Studying
Mtotal1 = math.floor(BMR) * Walking
Mtotal2 = math.floor(BMR) * Jogging 
Mtotal3 = math.floor(BMR) * BodyBuilding
Mtotal4 = math.floor(BMR) * Heavy_WeightLifting

# IF the users input matches "Male or male" print BMR 
if Gender == "Male" or Gender == "male": print(f"Your Basal Metabolic Rate: {math.floor(BMR)}")

# IF the activity is equal to "Daily Caloric Needs"
if (Gender == "Male" and 
    Activity == "Studying" or 
    Activity == "studying"): print(f"Your Total Daily Energy Expenditure: {Mtotal}")
if (Gender == "Male" and 
    Activity == "Walking" or 
    Activity == "walking"): print(f"Your Total Daily Energy Expenditure: {Mtotal1}")
if (Gender == "Male" and 
    Activity == "Jogging" or 
    Activity == "jogging"): print(f"Your Total Daily Energy Expenditure: {Mtotal2}")
if (Gender == "Male" and 
    Activity == "BodyBuilding" or
    Activity == "bodybuilding"): print(f"Your Total Daily Energy Expenditure: {Mtotal3}")
if (Gender == "Male" and 
    Activity == "Heavy WeightLifting" or 
    Activity == "heavyweightlifting"): print(f"Your Total Daily Energy Expenditure: {Mtotal4}")

# Females Daily Caloric Variables 
total = math.floor(BMR1) * Studying
total1 = math.floor(BMR1) * Walking
total2 = math.floor(BMR1) * Jogging
total3 = math.floor(BMR1) * BodyBuilding
total4 = math.floor(BMR1) * Heavy_WeightLifting


# IF the users input matches "Female or female" print BMR 
if (Gender == "Female" or 
    Gender == "female"): print(f"Your Basal Metabolic Rate: {math.floor(BMR1)}")
if (Activity == "Studying" or 
    Activity == "studying" and 
    Gender == "Female"): print(f"Your Total Daily Energy Expenditure: {total}")
if (Activity == "Walking" or 
    Activity == "walking" and 
    Gender == "Female"): print(f"Your Total Daily Energy Expenditure: {total1}")
if (Activity == "Jogging" or 
    Activity ==  "jogging" and 
    Gender == "Female"): print(f"Your Total Daily Energy Expenditure: {total2}")
if (Activity == "BodyBuilding" or 
    Activity == "bodybuilding" and 
    Gender == "Female"): print(f"Your Total Daily Energy Expenditure: {total3}")
if (Activity == "Heavy Weightlifting" or 
    Activity ==  "heavy weightlifting" and 
    Gender == "Female"): print(f"Your Total Daily Energy Expenditure: {total4}")


