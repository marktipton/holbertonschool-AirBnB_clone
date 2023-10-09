#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(self, *args, **kwargs)
