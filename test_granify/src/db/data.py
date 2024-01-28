from abc import ABC, abstractmethod
from src.db.fake_db import FakeDBClient

from src.model.i_animal import IAnimal


class IData(ABC):

    @abstractmethod
    def beginTran(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def insert(self, table, obj: IAnimal):
        pass


class Data(IData):
    def __init__(self):
        self.db = FakeDBClient()
        print("Connecting to database...")

    def beginTran(self):
        super().beginTran()
        print("Begin a transaction")

    def commit(self):
        super().commit()
        print("Committing transaction")

    def rollback(self):
        super().rollback()
        print("Rolling back transaction")

    def insert(self, table, obj: IAnimal):
        super().insert(table, obj)
        # self._arr_animals.append(obj)
        print("Inserting %s into table %s" % (obj.get_name(), table))
