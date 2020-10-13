# Calculating the BMR = 10 x Weight(kg) x Height(cm) - 5 x age(years) + 5
# Weight Variables Converting lbs to kg 
# BMR is an estimate of the amount of energy (calories) that your body expends when completely at rest. 
lbs = int(input("Enter Weight:"))
# Kilograms to pounds formula
kg = lbs / 2.2046226218
# Height Variables convert inches into cm
Height = "Please Enter Your Height in Feet & Inches:"
feet = int(input("Feet:"))
inches = int(input("Inches:"))
cm = feet * 12
cm1 = cm + inches
cm2 = cm1 * 2.54
import math
# Age Variables 
age = int(input("Enter Your Age:"))
# Gender Variable 
Gender = input("Male or Female:")
Male = "Male"
Female = "Female"
# BMR Variable
BMR = 10 * kg + 6.25 * cm2 - 5 * age + 5
BMR1 = 10 * kg + 6.25 * cm2 - 5 * age - 161

# Calculate Total Daily Caloric Needs 
Studying = 1.30
Walking = 1.55
Jogging = 1.65
BodyBuilding = 1.80
Heavy_WeightLifting = 2.00
TDCN = {Studying, Walking, Jogging, BodyBuilding, Heavy_WeightLifting}

Activity = input("Select Activity: Studying, Walking, Jogging, BodyBuilding, Heavy WeightLifting\n")

if Gender == "Male":
 print(f"Your Basal Metabolic Rate: {math.floor(BMR)}")
if Gender == "Male" and Activity == "Studying":
 Mtotal = math.floor(BMR) * Studying
 print(f"Your Total Daily Energy Expenditure: {Mtotal}")
if Gender == "Male" and Activity == "Walking":
 Mtotal1 = math.floor(BMR) * Walking
 print(f"Your Total Daily Energy Expenditure: {Mtotal1}")
if Gender == "Male" and Activity == "Jogging":
 Mtotal2 = math.floor(BMR) * Jogging 
 print(f"Your Total Daily Energy Expenditure: {Mtotal2}")
if Gender == "Male" and Activity == "BodyBuilding":
 Mtotal3 = math.floor(BMR) * BodyBuilding
 print(f"Your Total Daily Energy Expenditure: {Mtotal3}")
if Gender == "Male" and Activity == "Heavy WeightLifting":
 Mtotal4 = math.floor(BMR) * Heavy_WeightLifting
 print(f"Your Total Daily Energy Expenditure: {Mtotal4}")

if Gender == "Female":
 print(f"Your Basal Metabolic Rate: {math.floor(BMR1)}")

if Activity == "Studying" and Gender == "Female":
 total = math.floor(BMR1) * Studying
 print(f"Your Total Daily Energy Expenditure: {total}")

if Activity == "Walking" and Gender == "Female":
 total1 = math.floor(BMR1) * Walking 
 print(f"Your Total Daily Energy Expenditure: {total1}")
if Activity == "Jogging" and Gender == "Female":
 total2 = math.floor(BMR1) * Jogging
 print(f"Your Total Daily Energy Expenditure: {total2}")
if Activity == "BodyBuilding" and Gender == "Female": 
 total3 = math.floor(BMR1) * BodyBuilding
 print(f"Your Total Daily Energy Expenditure: {total3}")
if Activity == "Heavy Weightlifting" and Gender == "Female":
 total4 = math.floor(BMR1) * Heavy_WeightLifting
 print(f"Your Total Daily Energy Expenditure: {total4}")
