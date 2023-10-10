#!/usr/bin/python3
"""unittests for City"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCityDoc(unittest.TestCase):
    """check City documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(City.__doc__) > 0)


class TestCityPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/city.py'
            'tests/test_models/test_city.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


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
        self.assertEqual(issubclass(city.__class__, BaseModel))



if __name__ == "__main__":
    unittest.main()
