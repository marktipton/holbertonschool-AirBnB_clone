#!/usr/bin/python3
"""unittests for State"""
import unittest
import pycodestyle
from models.state import State
from datetime import datetime


class TestStateDoc(unittest.TestCase):
    """check State documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(State.__doc__) > 0)


class TestStatePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/base_model.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class TestState(unittest.TestCase):
    """tests for State"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        state = State()
        self.assertEqual(state.__class__.__name__, "State")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        state = State()
        self.assertEqual(state.__class__.__name__, "State")


if __name__ == "__main__":
    unittest.main()
