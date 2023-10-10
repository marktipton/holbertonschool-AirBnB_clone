#!/usr/bin/python3
"""unittests for State"""
import unittest
import pep8
from models.state import State
from datetime import datetime


class TestStateDoc(unittest.TestCase):
    """check State documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(State.__doc__) > 0)


class TestStatePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/state.py'
            'tests/test_models/test_state.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
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
