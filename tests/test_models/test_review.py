#!/usr/bin/python3
"""Module test_review of unittest class Review"""
import datetime
import pep8
import unittest
from models.review import Review


class testReview(unittest.TestCase):
    """Test cases for Review"""
    def setUp(self):
        """Sets up instances of the Review class"""
        self.reviewOne = Review()
        self.b_inst = Review()
        self.b_inst.save()

    def test_pep8(self):
        "Checks for pep8 styling"
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["./models/review.py"])
        self.assertEqual(result.total_errors, 0)

    def test_setup(self):
        """Tests for creating instances"""
        self.assertTrue(self.reviewOne.id != self.b_inst.id)
        self.assertTrue(hasattr(self.reviewOne, "updated_at"))
        self.assertTrue(hasattr(self.reviewOne, "place_id"))
        self.assertTrue(hasattr(self.b_inst, "place_id"))
        self.assertTrue(hasattr(self.reviewOne, "user_id"))
        self.assertTrue(hasattr(self.b_inst, "user_id"))
        self.assertTrue(hasattr(self.reviewOne, "text"))
        self.assertTrue(hasattr(self.b_inst, "text"))
        self.assertTrue(self.reviewOne.created_at != self.b_inst.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.reviewOne.created_at) is datetime.datetime)
        self.assertTrue(type(self.reviewOne.place_id) is str)
        self.assertTrue(type(self.reviewOne.user_id) is str)
        self.assertTrue(type(self.reviewOne.text) is str)

if __name__ == '__main__':
    unittest.main
