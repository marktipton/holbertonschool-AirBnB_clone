#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
from collections import OrderedDict


class BaseModel:
    """Base class for the console clone"""
    def __init__(self, *args, **kwargs):
        self.id = None
        self.created_at = None
        self.updated_at = None

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Reformating string repr"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updating the update_at attr with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Making a dictionary repr of this instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
