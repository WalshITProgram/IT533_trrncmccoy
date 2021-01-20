import unittest
from VariableSort import *


class TestVariableSort(unittest.TestCase):
    """ Test the VarableSort Class"""
    def setUp(self):
        """ Create an instance of the variable class functions"""
        self.string_ok = VariableSort("", "", "")
        self.number_ok = VariableSort("", "", "")
        self.flo_ok = VariableSort("", "", "")
    def testing_Validate_string(self):
        """Test validating string function"""
        self.string_ok.Validate_string("Bob")
        self.assertIn("cash", self.string_ok.Validate_string("cash"))

    def testing_Validate_int(self):
        """ Test validating integers function"""
        self.number_ok.Validate_integer(23)
        self.assertIn(23, self.number_ok.Validate_integer(23))
    def testing_Validate_Float(self):
        """ Test validating floating point function"""
        self.flo_ok.Validate_floating_number(3.2)
        self.assertIn(3.2, self.flo_ok.Validate_floating_number(3.2))

if __name__ == "__main__":
    unittest.main


