#!/usr/bin/python3
"""unittests for FileStorage"""
import unittest
import json
import os
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """instance for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """clean up after testing"""
        if os.path.exists(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def test_pycode(self):
        style = pycodestyle.StyleGuide(quiet=True)
        files = [
            'models/engine/file_storage.py'
            'tests/test_models/test_engine/test_file_storage.py'
        ]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )

    def test_documentation(self):
        check_class = [FileStorage]
        for cls in check_class:
            self.assertTrue(
                cls.__doc__ is not None and len(cls.__doc__strip()) > 0,
                f"Missing docstring in {cls.__name__}"
            )

    def test_all(self):
        """test all method"""
        test_dict = self.storage.all()
        self.assertIsInstance(test_dict, dict)

    def test_new(self):
        """tests if new method adds object correctly"""
        user = User()
        self.storage.new(user)
        key = "User." + str(user.id)
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        """test that save method serializes object correctly"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open(FileStorage.__file_path, 'r') as f:
            data = json.load(f)
        key = "User." + str(user.id)
        self.assertTrue(key in data)

    def test_reload(self):
        """tests deserialization of objects"""
        user = User()
        user_id = user.id
        self.storage.new(user)
        self.storage.save()

        self.storage.all().clear()
        self.storage.reload()
        key = "User." + str(user_id)
        self.assertTrue(key in self.storage.all())


if __name__ == '__main__':
    unittest.main()
