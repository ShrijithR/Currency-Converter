import unittest

from CurrencyToWords import Main_Function_Call
from src.support import Input_Validation
from src.support import Attrs

class TestConvert(unittest.TestCase):
    def test_Correct_A(self):
        self.convert_amount = Main_Function_Call('123456.78')
        self.assertEqual(
            self.convert_amount.convert(), 
            "Rs. One Lakh Twenty Three Thousand Four Hundred and Fifty Six 78/100 ONLY"
            )
    def test_Correct_B(self):
        self.validate = Input_Validation('90005.00')
        self.assertTrue(
            self.validate.validate()
            )
    def test_ToFloat(self):
        attr = Attrs('2340')
        self.assertIsInstance(attr.num_str, str)
        self.assertIsInstance(attr.num_list, list)
        self.assertIsInstance(attr.amount, int) 
    def test_Zero(self):
        self.convert_amount = Main_Function_Call('0')
        self.assertEqual(
            self.convert_amount.convert(),
            "Rs. Zero"
        )
    def test_InvalidCharacter(self):
        self.validate = Input_Validation('sdd')
        self.assertEqual(
            self.validate.validate(),
            "Invalid input"
        )
    def test_NumberOfDots(self):
        self.validate = Input_Validation('34.56.34')
        self.assertEqual(
            self.validate.validate(),
            "Invalid input"
        )
    def test_DecimalLimit(self):
        self.convert_amount = Main_Function_Call('234.5436')
        self.assertEqual(
            self.convert_amount.convert(),
            "Invalid input"
        )
    def test_StartWithDigit(self):
        self.convert_amount = Main_Function_Call('.05')
        self.assertEqual(
            self.convert_amount.convert(),
            "Invalid input"
        )
    def test_EndWithDigit(self):
        self.convert_amount = Main_Function_Call('0.3a')
        self.assertEqual(
            self.convert_amount.convert(),
            "Invalid input"
        )
    
if __name__ == "__main__":
    unittest.main()