import unittest
import sys

class TestVariableSort(unittest.TestCase):
    """ Test the VarableSort Class"""

    def Variable(self):
        """ Create an instance of the variable class functions"""
        self.my_variable = VariableSort("Jake","ggh","jkk")
    def testing_Validate_string(self):
        """Test validating string function"""
        self.my_variable.Validate_string("James")
        self.assertIn("Bobby", self.my_variable.string)
    def testing_Validate_int(self):
        """ Test validating integers function"""
        self.my_variable.Validate_integer()
    def testing_Validate_Float(self):
        """ Test validating floating point function"""
        self.my_variable.Validate_floating_number()
        


