##MUST START FILE NAME WITH TEST_ IN PYTHON
#reference pythonless8.py

#import unittest when using testing features of PYTHON
import unittest
from pythonlesson8 import Calculator

#unittest.TestCase is the class used to test classes
class CalculatorTests(unittest.TestCase):

    def setUp(self): #must be called setUp in PYTHON
        self.calculator = Calculator()
        #creating a property on the CalculatorTest class
        print("SETUP")
    def test_add_numbers(self): #can name function anything but must start with test_
        print("TESTING ADDITION")
        result = self.calculator.add(2,3)
        self.assertEqual(5,result)
        print("running test_add")
    def tearDown(self):  #runs after every test; must be tearDown()
        print("TEARDOWN")


#self.assertEqual() is imported from TestCase
#self.assertEqual tests if two values are equal (1 != 4 == FAIL)
#search for asserts on Google, along with the full unittest functions

unittest.main() #use to run all tests in this class
