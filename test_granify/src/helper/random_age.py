from abc import ABC, abstractmethod
import random


class IRandomAge(ABC):
    
    @abstractmethod
    def get_random_age(self):
        pass
    
    
class RandomAge(IRandomAge):
    
    def get_random_age(self):
        return random.randint(5,10)