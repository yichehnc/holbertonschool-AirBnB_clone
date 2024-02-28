#!/usr/bin/python3
"""Module User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This defines User Class.
    Attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
