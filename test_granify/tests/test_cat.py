import io
import sys
import unittest

sys.path.append("../test_granify")
from src.model.cat import Cat



class TestCat(unittest.TestCase):
    def test_cat_constructor(self):
        """Create a cat with default constructor should create the cat with the age between 5 and 10"""
        #arrange
        cat = Cat()
        
        # act
        age = cat.get_age()
        
        #assert
        self.assertTrue( age >= 5 and age <= 10)
    
    def test_cat_speak_by_default(self):
        """Call speak method in cat should print meow"""
        #arrange
        cat = Cat()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        
        # act
        cat.speak()
        sys.stdout = sys.__stdout__
        
        #assert
        result = capturedOutput.getvalue().rstrip('\n')
        
        self.assertEqual(result, "meow")
        
    def test_cat_speak_by_with_param(self):
        """Call speak method in cat should print the param sent to speak"""
        #arrange
        cat = Cat()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        
        # act
        cat.speak("Hello, I can talk")
        sys.stdout = sys.__stdout__
        
        #assert
        result = capturedOutput.getvalue().rstrip('\n')
        
        self.assertEqual(result, "Hello, I can talk")
        
    def test_cat_increase_age_after_call_speak(self):
        """Call speak method five times should increase the age in one"""
        #arrange
        cat = Cat()
        previous_age = cat.get_age()
        
        # ignoring print for speak
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        
        # act
        cat.speak()
        cat.speak()
        cat.speak()
        cat.speak()
        cat.speak()
        
        #assert
        self.assertEqual( previous_age + 1, cat.get_age())
        
    def test_cat_update_name(self):
        """After update the name the cat should have the new name"""
        #arrange
        cat = Cat("Beto")
        
        # act
        cat.set_name("Poncho")
        
        #assert
        self.assertEqual(cat.get_name(), "Poncho")
        
    def test_cat_update_name_keep_previous(self):
        """After update the name the cat should save all previous names"""
        
        #arrange
        cat = Cat("Magolo")
        
        # act
        cat.set_name("Poncho")
        
        #assert
        self.assertEqual(cat.get_names(), ["Magolo", "Poncho"])
        
        
    def test_cat_average_names(self):
        """After call get_average_name_length when the cat names is empty should show 0"""
        
        #arrange
        cat = Cat()
        
        # act
        
        #assert
        self.assertEqual(cat.get_average_name_length(), 0.0)
        
        
    def test_cat_average_names(self):
        """After update the name the cat should show the average of previous names length"""
        
        #arrange
        cat = Cat("Magolo")
        
        # act
        cat.set_name("Poncho")
        cat.set_name("Chammo")
        
        #assert
        self.assertEqual(cat.get_average_name_length(), 6)
        
        