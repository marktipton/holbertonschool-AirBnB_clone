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

    def save(self):
        """Updating the update_at attr with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Making a dictionary repr of this instance"""
        datetime = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict = OrderedDict()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["updated_at"] = self.updated_at.strftime(datetime)
        obj_dict["id"] = self.id
        obj_dict["created_at"] = self.created_at.strftime(datetime)
        obj_dict.update(self.__dict__)
        return obj_dict

    def __str__(self):
        """Reformating string repr"""
        obj_dict = self.to_dict()
        items = [
            f"{key}: {value} ({type(value)})" for key, value in obj_dict.items()
        ]
        return "[{self.__class__.__name__}] ( \
        {self.id}) " + '{' + ', '.join(items) + '}'
