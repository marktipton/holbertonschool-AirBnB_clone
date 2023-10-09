#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Class that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(self, *args, **kwargs)
