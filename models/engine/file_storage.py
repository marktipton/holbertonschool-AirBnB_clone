#!/usr/bin/python3
"""FileStorage that serializes to a JSON file and deserializes
files to instances"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj w/ key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(serialized_objects, json_file,
                      default=lambda x: x.__dict__)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for value in data.values():
                    obj_class = value["__class__"]
                    del value["__class__"]
                    if obj_class == User:
                        self.new(User(**value))
                    elif obj_class == State:
                        self.new(State(**value))
                    elif obj_class == City:
                        self.new(City(**value))
                    elif obj_class == Amenity:
                        self.new(Amenity(**value))
                    elif obj_class == Place:
                        self.new(Place(**value))
                    elif obj_class == Review:
                        self.new(Review(**value))
                    else:
                        pass
        except FileNotFoundError:
            pass
