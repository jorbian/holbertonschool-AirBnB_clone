#!/usr/bin/python3
"""
This is the class FileStorage that
serializes instances to a JSON file
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serialization/Deserialization of instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dict of __objects"""
        return self.__objects

    def new(self, obj):
        """Sets objects in dictionary with <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects dictionary to JSON path"""
        new = {}
        filename = self.__file_path
        for key, obj in self.__objects.items():
            new[key] = obj.to_dict()
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(json.dumps(new))

    def reload(self):
        """Deserializes of the JSON file to __objects dictionary"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
