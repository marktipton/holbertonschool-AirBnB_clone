#!/usr/bin/python3
"""unittests for BaseModel"""
import json
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for BaseModel"""
    def test_init(self):
        """test base constructor"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        """test save method"""
        base_model = BaseModel()
        before_update = base_model.updated_at
        base_model.save()
        self.assertNotEqual(before_update, base_model.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        base_model = BaseModel()
        inst_dict = base_model.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

    def test_str(self):
        """test __str__ method"""
        base_model = BaseModel()
        str_rep = str(base_model)
        self.assertIn(f"[BaseModel] ({base_model.id})", str_rep)


if __name__ == "__main__":
    unittest.main()
