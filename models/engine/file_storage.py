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
        return FileStorage.__objects

    def new(self, obj):
        """Sets objects in dictionary with <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects dictionary to JSON path"""
        new = {}
        filename = FileStorage.__file_path
        for key, obj in FileStorage.__objects.items():
            new[key] = obj.to_dict()
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(json.dumps(new))

    def reload(self):
        """Deserializes the JSON file to __objects dictionary"""
        obj = {}
        filename = FileStorage.__file_path
        try:
            with open(filename, 'r', encoding="UTF-8") as f:
                obj = json.load(f)
                for key, value in obj.items():
                    FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)
        except FileNotFoundError:
            pass
