#!/usr/bin/python3
"""unittest for BaseModel Class"""
import unittest
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel Class"""
    def test_base_save(self):
        """Test save method of BaseModel"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()  # obj
        my_model_json = my_model.to_dict()  # dict
        self.assertEqual(my_model.id, my_model_json["id"])


if __name__ == "__main__":
    unittest.main()
