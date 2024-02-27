#!/usr/bin/python3
"""Base Model Module"""
import uuid
import datetime


class BaseModel:
    """ BaseModel Class"""

    id = str(uuid.uuid4())

    created_at = datetime.datetime.today()
    updated_at = datetime.datetime.today()

    def __init__(self):
        """Initialisation of class attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = BaseModel.created_at
        self.updated_at = BaseModel.updated_at

    def __str__(self):
        """print string"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = BaseModel.updated_at

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            new_dict[key] = value
        return (new_dict)
