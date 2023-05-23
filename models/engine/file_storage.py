#!/usr/bin/python3
"""
This module contains the class and method that handle
serialization and desrilization of python objects
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Contains methods for serilization and desirilization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = {}
                for k, v in json.load(f).items():
                    json_dict[k] = eval(v['__class__'])(**v)
                self.__objects = json_dict
        except FileNotFoundError:
            pass
