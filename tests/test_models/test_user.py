#!/usr/bin/python3
"""unittests for User"""
import unittest
import pep8
from models.user import User
from datetime import datetime


class TestUserDoc(unittest.TestCase):
    """check User documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/user.py'
            'tests/test_models/test_user.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


class TestUser(unittest.TestCase):
    """tests for User"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_save(self):
        """test save method"""
        user = User()
        before_update = user.updated_at
        user.save()
        self.assertNotEqual(before_update, user.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        user = User()
        inst_dict = user.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "User")
        self.assertEqual(
            inst_dict["created_at"], user.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], user.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        user = User()
        str_rep = str(user)
        self.assertIn(f"[User] ({user.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = User()
        base_2 = User()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = User(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = User(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = User()
        serialized_data = base_1.to_dict()
        deserialized_base = User(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
