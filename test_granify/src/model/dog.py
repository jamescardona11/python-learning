
from src.model.i_animal import IAnimal


class Dog(IAnimal):
    def __init__(self, name=None):
        super(Dog, self).__init__(name)

    def speak(self, arg=None):
        super().speak(arg)
        print("guau!!")
