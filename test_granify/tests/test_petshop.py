import sys
import unittest
from unittest.mock import patch

sys.path.append("../test_granify")
from src.db.data import IData
from src.shop.pet_shop import PetShop
from src.model.i_animal import IAnimal


class MockData(IData):
    def beginTran(self):
        super().beginTran()
        pass

    def commit(self):
        super().commit()
        pass

    def rollback(self):
        super().rollback()
        pass

    def insert(self, table, obj: IAnimal):
        super().insert(table, obj)
        print("is_called")


class TestPetShop(unittest.TestCase):
    
    @patch.object(MockData, "insert")
    def test_save_test_insert_animals(self, mock):
        # arrange
        mockData = MockData()
        pet = PetShop(mockData)
            
        # act
        pet.save_test()
        
        mock.assert_called()
        
        
    @patch.object(MockData, "insert")
    def test_save_pet_shop_insert_animals(self, mock):
        # arrange
        mockData = MockData()
        pet = PetShop(mockData)
            
        # act
        pet.save_pet_shop()
        
        # assert
        mock.assert_called()