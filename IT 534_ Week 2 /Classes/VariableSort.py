import pydoc
class VariableSort(): 
    def __init__(self, word, number, point):
        """ Create Constructor for VariableSort Class"""
        self.word = word
        self.number = number
        self.point = point
    
    def Validate_string(self, word):
        """ Create a function to determine if the string is valid"""
        try:
            if str(word):
                if word.isalpha():
                    string = []
                    string.append(word)
        except AttributeError:
            print("Wrong Data Type!") 
        
    def Validate_integer(self, number):
        """ Create a function to determine if the input is a integer"""
        try:
            if int(digit):
                if digit.isdigit():
                    number = []
                    number.append(digit)
        except ValueError:
            print("")
    def Validate_floating_number(self, point):
        """ Create a function to determine if the input is a float"""
        try:
            if float(point):
                floating_point = [] 
                floating_point.append(point)
        except ValueError:
            print("")

    

