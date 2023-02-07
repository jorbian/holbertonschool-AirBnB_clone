#!/usr/bin/python3
"""tests FileStorage class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import pep8
import unittest
import sys

sys.exit()

class FileStorage(unittest.TestCase):
    """tests for FileStorage"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_FileStorage(self):
        """check for attributes"""
        self.assertTrue(FileStorage.__file_path.__doc__)
        self.assertTrue(FileStorage.__objects.__doc__)

    def test_all(self):
        """check for returns the dictionary __objects"""
        pass

    def test_new(self):
        """check for setting the objects in __objects dictionary"""
        pass

    def test_save(self):
        """check if it saves changes"""
        Storage = FileStorage()
        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """check for deserializes the JSON file to __objects"""
        pass
