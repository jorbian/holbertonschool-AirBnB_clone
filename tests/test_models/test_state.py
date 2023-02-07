#!/usr/bin/python3
"""module test_state of unittest class State"""
import pep8
import unittest
from models.state import State


class testState(unittest.TestCase):
    """Test cases of state"""

    def setUp(self):
        """Sets up objects for testing"""
        self.stateOne = State()
        self.stateTwo = State()

    def test_pep8(self):
        """Checks for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type(self):
        """Tests the type"""
        self.assertEqual(type(self.stateOne.name), str)
        self.assertEqual(type(self.stateTwo.name), str)
        self.assertIsInstance(self.stateOne, State)
        self.assertIsInstance(self.stateTwo, State)

    def test_attribute(self):
        """Tests the attributes"""
        self.assertTrue(hasattr(self.stateTwo, "name"))
        self.assertFalse(hasattr(self.stateOne, "text"))
        self.assertTrue(hasattr(self.stateOne, "name"))
        self.assertFalse(hasattr(self.stateTwo, "user_id"))
        self.assertTrue(self.stateOne != self.stateTwo)

if __name__ == '__main__':
    unittest.main()
