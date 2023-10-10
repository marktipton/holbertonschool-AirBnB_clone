#!/usr/bin/python3
"""unittests for Amenity"""
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenityDoc(unittest.TestCase):
    """check Amenity documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Amenity.__doc__) > 0)


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
        self.assertTrue(issubclass(amenity.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
