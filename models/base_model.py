#!/usr/bin/python3
"""Base Model Module"""
import uuid
import datetime


class BaseModel:
    """ BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialisation of class attributes"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.now()
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """print string"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.datetime.now()

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
