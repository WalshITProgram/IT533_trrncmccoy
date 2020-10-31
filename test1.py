employee_dict = {}

valid_name_chars = ['A','B','C','D','a','b','c','d','-', ' ', '\'']

while True:
	entered_name = input("Enter your name")
	bad_char_hit = False
	for letter in entered_name:
		if letter not in valid_name_chars:
			bad_char_hit = True

	if bad_char_hit == False:
		employee_dict['Name'] = entered_name
		break