import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        
        #Arrange
        first = 2
        second = 3
        
        #Act
        result = maths.add(first, second)
        
        #Assert
        self.assertEqual(result, 5)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        
        #Arrange
        num_lenght = 5
        
        #Act
        result = maths.fibonacci(num_lenght)
        
        #Assert
        self.assertEqual(result, 5)
        
    def test_convert_base1(self):
        
        #Arrange
        num = 15
        n = 2
        
        #Act
        result = maths.convert_base(num, n)
        
        #Assert
        self.assertEqual(result,'1111')
        
    def test_convert_base2(self):
        
        #Arrange
        num = 15
        n = 16
        
        #Act
        result = maths.convert_base(num, n)
        
        #Assert
        self.assertEqual(result,'F')
        
    def test_optional_parameter_add(self):
        
        #Arrange
        first = 10
        second = 5
        n = 2
        
        #Act
        result = maths.add(first, second, n)
        
        #Assert     
        self.assertEqual(result, '1111')

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
