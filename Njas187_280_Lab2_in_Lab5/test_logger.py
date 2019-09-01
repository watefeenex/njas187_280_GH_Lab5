import unittest
import logger
from logger import Logger

class loggerTest(unittest.TestCase):
    
    def test_init(self):
        
        #Arrange
        name = Logger('Nipun')
        
        #Act
        #Not needed
        
        #Assert
        self.assertEqual(name._target, 'Nipun')
        
    def test_info(self):
        
        #Arrange
        name = Logger('Nipun')
        
        #Act
        name.info('It works!')
        
        #Assert
        self.assertEqual(name._target, '[INFO] It works!' )
        
        
    def test_error(self):
        
        #Arrange
        name = Logger('Nipun')
        
        #Act
        name.error('You have done something wrong.')
        
        #Assert
        self.assertEqual(name._target, '[WARNING] You have done something wrong.' )
        
if __name__ == '__main__':
    unittest.main()