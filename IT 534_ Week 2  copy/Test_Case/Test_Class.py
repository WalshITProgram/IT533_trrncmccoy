import unittest
from VariableSort import VariableSort

class TestVariableSort(unittest.TestCase):
    """ Test the VarableSort Class"""

    def Variable(self):
        """ Create an instance of the variable class functions"""
        self.my_variable = VariableSort("","","")
    def testing_Validate_string(self):
        """Test validating string function"""
        self.my_variable.Validate_string("James")
    def testing_Validate_int(self):
        """ Test validating integers function"""
        self.my_variable.Validate_integer(5)
    def testing_Validate_Float(self):
        """ Test validating floating point function"""
        self.my_variable.Validate_floating_number(8.4)
        


