#!/usr/bin/python3
"""unittests for BaseModel"""
import unittest
import pycodestyle
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelDoc(unittest.TestCase):
    """check BaseModel documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)


class TestBasePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        files = [
            'models/base_model.py',
            'tests/test_models/test_base_model.py'
        ]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


class TestBaseModel(unittest.TestCase):
    """tests for BaseModel"""
    def setUp(cls):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

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

        self.assertEqual(inst_dict["__class__"], "BaseModel")
        self.assertEqual(
            inst_dict["created_at"], base_model.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], base_model.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        base_model = BaseModel()
        str_rep = str(base_model)
        self.assertIn(f"[BaseModel] ({base_model.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = BaseModel(id="")
        self.assertEqual(base_1.id, "")

    def test_id(self):
        """test id method"""
        base1 = BaseModel()
        self.assertEqual(str, type(base1.id))

    def test_updated_at(self):
        """test updated_at method"""
        base1 = BaseModel()
        self.assertEqual(datetime, type(base1.updated_at))

    def test_created_at(self):
        """test created_at method"""
        base1 = BaseModel()
        self.assertEqual(datetime, type(base1.created_at))

    def test_to_dict(self):
        """test to_dict method"""
        base1 = BaseModel()
        dict1 = base1.to_dict()
        self.assertEqual(type(dict1), dict)


if __name__ == "__main__":
    unittest.main()
