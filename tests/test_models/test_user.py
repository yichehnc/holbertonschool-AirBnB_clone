import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test case for User Class"""
    def test_user(self):
        """Test for User Class"""
        my_user = User()
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")


if __name__ == "__main__":
    unittest.main()
