#!/usr/bin/python3
"""unittest for FileStorage Class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage Class"""
    def test_all(self):
        """Test all method"""
        my_model = BaseModel()
        my_model.save()
        all_objs = storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertEqual(my_model.id, all_objs[key].__dict__['id'])

    def test_save(self):
        """
        Test for save() method
        """
        object_1 = BaseModel()
        object_1.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))



if __name__ == "__main__":
    unittest.main()
