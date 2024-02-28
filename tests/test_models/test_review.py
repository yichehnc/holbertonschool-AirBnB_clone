import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for Review Class"""
    def test_review(self):
        """Test for Review Class"""
        my_review = Review()
        self.assertEqual(my_review.text, "")


if __name__ == "__main__":
    unittest.main()
