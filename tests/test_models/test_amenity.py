import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for Amenity Class"""
    def test_amenity(self):
        """Test for Amenity Class"""
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")


if __name__ == "__main__":
    unittest.main()
