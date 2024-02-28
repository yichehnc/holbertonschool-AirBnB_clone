#!/usr/bin/python3
"""Module City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This defines City Class.
    Attributes:
    state_id: string - empty string
    name: string - empty string
    """
    state_id = ""
    name = ""
