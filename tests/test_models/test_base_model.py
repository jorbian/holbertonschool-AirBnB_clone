#!/usr/bin/python3
"""tests BaseModel class"""

from datetime import datetime
from models.base_model import BaseModel

import unittest

class TestBaseModel(unittest.TestCase):
    """tests for BaseModel class"""
    
    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_BaseModelsMethods(self):
        """check for methods"""
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def Test_BaseModel_Clss(self):
        """check for subclass of Superclass"""
        my_model = BaseModel()
        self.assertTrue(my_model, "__class__")
        self.assertTrue(my_model, "id")
        self.assertTrue(my_model, "created_at")
        self.assertTrue(my_model, "updated_at")

    def Test_BaseModel_str_cls(self):
        """check for representation string for class"""
        my_model = BaseModel()
        self.assertEqual("[BaseModel]" in str(my_model), true)
        my_model = BaseModel()
        self.assertEqual("id" in str(my_model), true)
        my_model = BaseModel()
        self.assertEqual("created_at" in str(my_model), true)
        my_model = BaseModel()
        self.assertEqual("updated_at" in str(my_model), true)

    def Test_BaseModel_save(self):
        """check for update_at with the current datetime"""
        my_model = BaseModel()
        my_model.save()
        self.assertTrue(my_model, "updated_at")

    def Test_BaseModel_to_dict(self):
        """check for dictionary that contains all keys/values"""
        my_model = BaseModel()
        new = self.my_model.to_dict()
        self.asserTrue("to_dict" in dir(self.my_model))

    def test_BaseModel_id(self):
        """checks for id"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(type(my_model.id), str)

if __name__ == "__main__":
    unittest.main()
