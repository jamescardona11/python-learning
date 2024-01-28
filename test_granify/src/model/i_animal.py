from abc import ABC, abstractmethod


class IAnimal(ABC):
    def __init__(self, name=None, age=None, favorite_food=None):
        self._name = name
        self._age = age
        self._favorite_food = favorite_food

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_favorite_food(self):
        return self._favorite_food

    def set_name(self, name):
        self._name = name
        

    def set_age(self, age):
        self._age = age

    def set_favorite_food(self, food):
        self._favorite_food = food

    @abstractmethod
    def speak(self, arg=None):
        pass

    def __str__(self):
        return f"Animal: name={self._name}, age={self._age}, favorite_food={self._favorite_food}"
