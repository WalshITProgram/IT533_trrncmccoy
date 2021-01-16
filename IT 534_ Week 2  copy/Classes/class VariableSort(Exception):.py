class VariableSort(Exception): 
    def __init__(self, word, number, point):
        self.word = word
        self.number = number
    

    def Validate_string(self, word):
        try:
            if str(word):
                if word.isalpha():
                    return word
        except AttributeError:
            print("Wrong Data Type!") 
        
    def Validate_integer(self, number):
        try:
            if int(number):
                if number.isdigit():
                    return number
        except ValueError:
            print("Enter number!")
    def Validate_floating_number(self, point):
        try:
            if float(point):
                return point
        except ValueError:
            print("Enter Decimal!")