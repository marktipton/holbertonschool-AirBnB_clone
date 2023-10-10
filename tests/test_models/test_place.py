#!/usr/bin/python3
"""unittests for Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlaceDoc(unittest.TestCase):
    """check Place documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Place.__doc__) > 0)


class TestPlacePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/place.py'
            'tests/test_models/test_place.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )
class TestPlace(unittest.TestCase):
    """tests for Place"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        place = Place()
        self.assertEqual(place.__class__.__name__, "Place")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        place = Place()
        self.assertEqual(issubclass(place.__class__, BaseModel))



if __name__ == "__main__":
    unittest.main()
