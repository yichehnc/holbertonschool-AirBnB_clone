import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case for Place Class"""
    def test_place(self):
        """Test for Place Class"""
        my_place = Place()
        self.assertEqual(my_place.name, "")


if __name__ == "__main__":
    unittest.main()
