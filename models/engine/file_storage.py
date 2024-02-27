#!/usr/bin/python3
"""File storage to serialize and deserialize instances to a JSON file"""
import json


class Filestorage:
    """
    Serialize or deserialize data
    Attributes:
    __file_path(string): path to the JSON file (ex: file.json)
    __objects(dictionary): empty but store all objects by id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
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
        reloaded_dict = {}
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                reloaded_dict = json.load(file)
        except Exception:
            pass
        for key, dict in reloaded_dict.items():
            self.__objects[key] = BaseModel(**dict)
        # create an object based on the dict
