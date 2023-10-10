#!/usr/bin/python3
"""Package for FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

    def reload(self):
        """Deserializes the JSON file to __objects"""
        class_mapping = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for value in data.values():
                    obj_class_name = value.get("__class__")
                    if obj_class_name in class_mapping:
                        del value["__class__"]
                        obj_class = class_mapping[obj_class_name]
                        try:
                            obj = obj_class(**value)
                            self.new(obj)
                        except Exception as e:
                            print(f"Error creating object: {e}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading data from JSON: {e}")
