#!/usr/bin/python3
"""unittest for State Class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case for State Class"""
    def test_state(self):
        """Test for State Class"""
        my_state = State()
        self.assertIsInstance(my_state, State)


if __name__ == "__main__":
    unittest.main()
