#!/usr/bin/python3
"""unittests for Amenity"""
import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenityDoc(unittest.TestCase):
    """check Amenity documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestAmenityPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/amenity.py'
            'tests/test_models/test_amenity.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


class TestAmenity(unittest.TestCase):
    """tests for Amenity"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        amenity = Amenity()
        self.assertEqual(issubclass(amenity.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
