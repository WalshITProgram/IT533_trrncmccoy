Health_dict = {}
while True:
    name = input("Name:")
    if len(name) == 0:
        continue
    bad_char = False
    for x in name:
        if x.isalpha():
            Health_dict["Name"] = name 
    Body_weight = input("Weight:")
    try:
        if int(Body_weight):
            kg_weight = round(int(Body_weight) / 2.2046)

    except:
        TypeError
    height = input("Feet:")
    inches = input("Inches:")
    try:
        if int(height) and int(inches):
            cm = round(int(height) * 30.48 + int(inches) * 2.54)
    except:
        NameError
    age = input("Age:")
    try:
        int(age)
        Health_dict["Age"] = age
    except:
        TypeError
    Rate = input("Level of Intensity on a scale:\n Sedentary - 1.2\n Lightly Active - 1.375\n Moderately Active - 1.55\n Very Active - 1.735\n Extremely Active - 1.9\n")
    
   
    Protein = 0.40
    Carbs = 0.25
    Fat = 0.35
    cm = round(int(height) * 30.48 + int(inches) * 2.54)

    gender = input("female or male:")
    if gender == "male" and float(Rate):   
        Mens_BMR = round((10 * kg_weight) + (6.25 * cm) - (5 * int(age) + 5))
        Health_dict['BMR'] = Mens_BMR
        BMR_CAL = round(Mens_BMR * float(Rate))
        Health_dict['BMR Activity Calories'] = BMR_CAL
        Calories_Protein = Mens_BMR * Protein
        Per_day = Calories_Protein/4
        Health_dict["Protein Per Day"] = round(Per_day)
        calorie_carb = Mens_BMR * Carbs
        Carb_day = calorie_carb/4
        Health_dict["Carbs Per day"] = round(Carb_day)
        calorie_Fat = Mens_BMR * Fat
        Fat_day = calorie_Fat/9
        Health_dict["Fat Per Day"] = round(Fat_day)


    elif gender == "female":
        Womens_BMR = round((10 * kg_weight) + (6.25 * cm) - (5 * int(age) - 161))
        Health_dict['BMR'] = Womens_BMR
        BMR_CAL = round(Womens_BMR * float(Rate))
        Health_dict['Total Daily Energy Expenditure'] = BMR_CAL
        Calories_Protein = Womens_BMR * Protein
        Per_day = Calories_Protein/4
        Health_dict["Protein Per Day"] = round(Per_day) 
        calorie_carb = Womens_BMR * Carbs
        Carb_day = calorie_carb/4
        Health_dict["Carbs Per Day"] = Carb_day
        calorie_Fat = Womens_BMR * Fat
        Fat_day = calorie_Fat/9
        Health_dict["Fat Per Day"] = round(Fat_day)
    user = input("Would you like to enter another record?")
    if user == "no":
        break
        

print(Health_dict)

    


