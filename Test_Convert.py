import unittest
import time
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
        self.convert_amount = Main_Function_Call('sdd')
        self.assertEqual(
            self.convert_amount.convert(),
            "sdd contains invalid input character"
        )
    def test_NumberOfDots(self):
        self.convert_amount = Main_Function_Call('34.56.34')
        self.assertEqual(
            self.convert_amount.convert(),
            "34.56.34 contains invalid input character"
        )
    def test_DecimalLimit(self):
        self.convert_amount = Main_Function_Call('234.5436')
        self.assertEqual(
            self.convert_amount.convert(),
            "234.5436 contains invalid input character"
        )
    def test_StartWithDigit(self):
        self.convert_amount = Main_Function_Call('.05')
        self.assertEqual(
            self.convert_amount.convert(),
            ".05 contains invalid input character"
        )
    def test_EndWithDigit(self):
        self.convert_amount = Main_Function_Call('0.3a')
        self.assertEqual(
            self.convert_amount.convert(),
            "0.3a contains invalid input character"
        )
    def test_Limit(self):
        self.convert_amount = Main_Function_Call('9999789')
        self.assertEqual(
            self.convert_amount.convert(),
            "9999789 is not in between 0 and 999999.99"
        )
    
if __name__ == "__main__":
    unittest.main()
    time.sleep(3)

