#!/usr/bin/python3
"""unittest for BaseModel Class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel Class"""
    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_reload(self):
        """Test reload method"""
        my_model = BaseModel()
        my_model.save()
        all_objs = storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertEqual(my_model.id, all_objs[key].__dict__['id'])

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()  # obj
        my_model_json = my_model.to_dict()  # dict
        self.assertEqual(my_model.id, my_model_json["id"])
    
    def test_str(self):
        """Test __str__ method"""
        my_model = BaseModel()
        str_format = ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))
        self.assertEqual(type(str(my_model)), type(str_format))

    def test_init(self):
        """Test __init__ method"""
        my_model = BaseModel()
        self.assertNotEqual(my_model.id, "")
        self.assertNotEqual(my_model.created_at, "")
        self.assertNotEqual(my_model.updated_at, "")


if __name__ == "__main__":
    unittest.main()
