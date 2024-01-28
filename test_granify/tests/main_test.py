import unittest

from test_cat import TestCat
from test_petshop import TestPetShop
from test_random import TestRandomAge


if __name__ == "__main__":
    unittest.main()
    TestRandomAge()
    TestCat()
    TestPetShop()