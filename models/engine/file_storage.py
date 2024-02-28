#!/usr/bin/python3
"""This module creates FileStorage class"""
import json


class FileStorage:
    """
    This defines FileStorage Class

    Attributes:
    __file_path(string): path to the JSON file
    __objects(dictionary): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Arg:
        obj(object): object to be set into __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj  # an object not the dictionary

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        reloaded_dict = {}
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                reloaded_dict = json.load(file)
        except Exception:
            pass
        for key, dict in reloaded_dict.items():
            # create an object based on the dict
            self.__objects[key] = class_dict[dict["__class__"]](**dict)
