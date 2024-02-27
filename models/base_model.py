#!/usr/bin/python3
"""This module creates BaseModel class"""
import uuid
import datetime
from models import storage


class BaseModel:
    """This defines BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initialisation of the BaseModel Class"""
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
            storage.new(self)

    def __str__(self):
        """Return the string representation of BaseModel Class"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

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
