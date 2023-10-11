#!/usr/bin/python3
"""unittests for User"""
import unittest
import pycodestyle
from models.user import User
from datetime import datetime


class TestUserDoc(unittest.TestCase):
    """check User documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/user.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class TestUser(unittest.TestCase):
    """tests for User"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        user = User()
        self.assertEqual(user.__class__.__name__, "User")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        user = User()
        self.assertEqual(user.__class__.__name__, "User")


if __name__ == "__main__":
    unittest.main()
