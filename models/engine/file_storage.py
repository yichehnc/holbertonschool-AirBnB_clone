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
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    self.__objects[key] = value
        except Exception:
            pass
