#!/usr/bin/python3
"""FileStorage that serializes to a JSON file and deserializes
files to instances"""
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj w/ key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
