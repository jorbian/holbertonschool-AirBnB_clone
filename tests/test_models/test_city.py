#!/usr/bin/python3
"""Tests for City class"""

from models.city import City
from models.base_model import BaseModel
import unittest
import json
import pep8


class City_Tests(unittest.TestCase):
    """Test cases for City class"""

    def test_pep8(self):
        """Checks for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_City_clss(self):
        """Checks for class existence"""
        self.assertTrue(City.__doc__)

    def test_set_attr(self):
        """Checks for public class attributes"""
        self.city = City()
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "id"))

    def test_user_attributes(self):
        """Tests for attributes"""
        self.city = City()
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

if __name__ == '__main__':
    unittest.main()
