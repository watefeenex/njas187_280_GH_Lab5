import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class FactorialTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_factorial(self):
        ''' Tests the factorial function. '''
        
        #Arrange
        num = 3
        
        #Act
        result = maths.factorial(num)
        
        #Assert
        self.assertEqual(result, 6)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
