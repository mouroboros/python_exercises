import unittest


class LeapTestCase(unittest.TestCase):
    def test_1990_is_not_leap(self):
        self.assertFalse(leap(1990))
    def test_2000_is_leap(self):
        self.assertTrue(leap(2000))

    def test_2024_is_leap(self) :
        self.assertTrue(leap(2024))

#The year can be evenly divided by 4;
#If the year can be evenly divided by 100, it is NOT a leap year, unless;
#The year is also evenly divisible by 400. Then it is a leap year.

def leap(year) :
    #The year can be evenly divided by 4;
    if year % 4 == 0 : return True
    elif year % 400 == 0 : return True
    else : return False
    
#If the year can be evenly divided by 100, it is NOT a leap year, unless;
#The year is also evenly divisible by 400. Then it is a leap year.


unittest.main()
