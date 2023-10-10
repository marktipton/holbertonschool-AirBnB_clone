#!/usr/bin/python3
"""unittests for City"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCityDoc(unittest.TestCase):
    """check City documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(City.__doc__) > 0)


class TestCity(unittest.TestCase):
    """tests for City"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        city = City()
        self.assertEqual(city.__class__.__name__, "City")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
