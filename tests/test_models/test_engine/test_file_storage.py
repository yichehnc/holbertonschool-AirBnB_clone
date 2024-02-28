#!/usr/bin/python3
"""unittest for FileStorage Class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage Class"""
    def setUp(self):
        """
        Setup for FileStorage
        """
        self.storage = FileStorage()

    def test_all(self):
        """Test all method"""
        my_model = BaseModel()
        my_model.save()
        all_objs = storage.all()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertEqual(my_model.id, all_objs[key].__dict__['id'])

    def test_reload(self):
        """
        Test for reload() method
        """
        object_1 = BaseModel()
        self.storage.new(object_1)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = object_1.__class__.__name__ + "." + object_1.id
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
