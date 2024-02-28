#!/usr/bin/python3
"""unittest for FileStorage Class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage Class"""
    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        my_model.save()
        with open ('file.json', 'r', encoding='UTF-8') as file:
            self.assertNotEqual(len(file.read()), 0)
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
