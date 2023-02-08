#!/usr/bin/python3
"""Unit test for User class"""
import unittest
import models
import os
from datetime import datetime
from models.user import User


class TestUserModel(unittest.TestCase):
    """Test cases for User class"""
    def test_init(self):
        """Tests class"""
        self.assertEqual(User, type(User()))

    def test_email_pub(self):
        """Tests email type"""
        self.assertEqual(str, type(User.email))

    def test_paswd_pub(self):
        """Tests password type"""
        self.assertEqual(str, type(User.password))

    def test_fname_pub(self):
        """Tests first_name type"""
        self.assertEqual(str, type(User.first_name))

    def test_lname_pub(self):
        """Tests last_name type"""
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
