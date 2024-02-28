import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for City Class"""
    def test_city(self):
        """Test for City Class"""
        my_city = City()
        self.assertEqual(my_city.name, "")


if __name__ == "__main__":
    unittest.main()
