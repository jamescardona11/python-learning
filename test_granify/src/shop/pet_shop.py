from abc import ABC, abstractmethod

from src.model.cat import Cat
from src.model.dog import Dog
from src.db.data import IData
from src.model.i_animal import IAnimal


class IPetShop(ABC):
    def __init__(self, database: IData):
        self._data = database

    @abstractmethod
    def save_test(self):
        self.log_stats("starting the execution of save_test method")
        pass

    @abstractmethod
    def save_pet_shop(self):
        self.log_stats("starting the execution of save_pet_shop method")
        pass
    
    
    def log_stats(self, log):
        f = open("logs.txt", "a+")
        f.write(f"{log}\n")
        f.close()


class PetShop(IPetShop):
    def save_test(self):
        super().save_test()
        cat = Cat("Jacinto")
        dog = Dog("halley")

        self.log_stats(self._action_to_log(cat))
        self.log_stats(self._action_to_log(dog))
        
        self.log_stats("finished the execution of save_test method")

    def save_pet_shop(self):
        super().save_pet_shop()
        arr = [Cat(), Cat(), Cat(), Dog(), Dog(), Dog()]
        
        self.log_stats("starting cycle to insert the arr with animals")
        for val in arr:
            self.log_stats(self._action_to_log(val))
            
        self.log_stats("finished the execution of save_pet_shop method")
        
    def _action_to_log(self, obj: IAnimal) -> str:
        if obj is Cat:
            self._data.insert("Cat", obj)
            return "insert a cat to data"
        else: 
            self._data.insert("Dog", obj)
            return "insert a dog to data"


        
