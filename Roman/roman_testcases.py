
import unittest

def roman (number):
    numeral = ''
    if number < 5 : 
        for x in range(number) :
            numeral += "I"
    else : numeral = "V"
    return numeral
    
class roman_numeral_testcases (unittest.TestCase) :
    # notice the roman numeral is a string.
    # so you need to build strings
    # "I" + "I" -> "II"
    def test_1_is_I(self):
        self.assertEqual(roman(1), 'I')
        
    def test_2_is_II(self):
        self.assertEqual(roman(2), 'II')

    def test_3_is_III(self):
        self.assertEqual(roman(3), 'III')
        
    def test_5_is_V(self):
        self.assertEqual(roman(5), 'V')
    # what next ??

   

unittest.main()
