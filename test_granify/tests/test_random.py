
import sys
import unittest

sys.path.append("../test_granify")
from src.helper.random_age import RandomAge

class TestRandomAge(unittest.TestCase):

    def test_random_age_creation(self):
        """Should return a number between 5 and 10"""
        #arrange
        random = RandomAge()
        
        # act
        result = random.get_random_age()
        
        #assert
        self.assertTrue( result >= 5 and result <= 10)
        
    

