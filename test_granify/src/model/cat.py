from functools import reduce
from src.helper.random_age import RandomAge
from src.model.i_animal import IAnimal


class Cat(IAnimal, RandomAge):
    def __init__(self, name=None):
        super(Cat, self).__init__(name, age=self.get_random_age())
        self._list_names = [name] if name is not None else []
        self._speak_time = 0

    def speak(self, arg=None):
        super().speak(arg)
        if arg is not None:
            print(arg)
        else:
            print("meow")

        self.__increase_age()

    def set_name(self, name):
        super().set_name(name)
        self._list_names.append(name)

    def get_names(self):
        return self._list_names

    def get_average_name_length(self):
        if len(self._list_names) == 0:
            return 0
        else:
            return (self.__get_reduce_val()) / len(self._list_names)

    def __get_reduce_val(self):
        return reduce(lambda a, e: a + len(e), self._list_names, 0)

    def __increase_age(self):
        self._speak_time += 1
        if self._speak_time >= 5:
            self._speak_time = 0
            self.set_age(self.get_age() + 1)
