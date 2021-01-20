import pydoc
class VariableSort(Exception): 
    def __init__(self, word, digit, point):
        """ Create Constructor for VariableSort Class"""
        self.word = word
        self.digit = digit
        self.point = point
    
    def Validate_string(self, word):
        """ Create a function to determine if the string is valid"""
        string = []
        try:
            if str(word):
                if word.isalpha():
                    string.append(word)
        except AttributeError:
            print("Wrong Data Type!") 
        
    def Validate_integer(self, digit):
        """ Create a function to determine if the input is a integer"""
        number = []
        try:
            if int(digit):
                if digit.isdigit():
                    number.append(digit)
        except ValueError:
            print("")
    def Validate_floating_number(self, point):
        """ Create a function to determine if the input is a float"""
        floating_point = []
        try:
            if float(point):
                floating_point.append(point)
        except ValueError:
            print("")

    

