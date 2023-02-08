#!/usr/bin/python3
"""FileStorage Unit Test Module"""
import unittest
import os
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """file storage unit tests"""
    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def test_all(self):
        """Tests all module"""
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(obj, objects["BaseModel.{}".format(obj.id)])

    def test_new(self):
        """Tests making a new obj"""
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertEqual(obj, objects["BaseModel.{}".format(obj.id)])

    def test_save(self):
        """Tests saving an obj"""
        obj = BaseModel()
        self.file_storage.new(obj)
        self.file_storage.save()
        with open(self.file_path, "r") as file:
            file_content = json.load(file)
        self.assertEqual(obj.to_dict(),
                        file_content["BaseModel.{}".format(obj.id)])

    def test_reload(self):
        """Tests reloading an object"""
        FileStorage.clear()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)

    def tearDown(self):
        """Tests tearing down an obj"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


if __name__ == "__main__":
    unittest.main()
