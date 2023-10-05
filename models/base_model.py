#!/usr/bin/python3
"""Base Model"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Base class for the console clone"""
    def __init__(self, *args, **kwargs):
        """Assigning a unique ID as a string"""
        unique_id = str(uuid.uuid4())

        """Assign current date and time"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updating the update_at attr with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Making a dictionary repr of this instance"""
        obj_dict = self.__dict__.copy()

        """Add __class__ key with the calss name"""
        obj_dict["__class__"] = self.__class__.__name__

        """Convert instance attr to ISO format"""
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.created_at.isoformat()

        return obj_dict

    def __str__(self):
        """Reformating string repr"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
