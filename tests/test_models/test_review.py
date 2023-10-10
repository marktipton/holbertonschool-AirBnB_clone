#!/usr/bin/python3
"""unittests for Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReviewDoc(unittest.TestCase):
    """check Review documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Review.__doc__) > 0)


class TestReview(unittest.TestCase):
    """tests for Review"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_class(self):
        """Tests if correct class"""
        review = Review()
        self.assertEqual(review.__class__.__name__, "Review")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        review = Review()
        self.assertTrue(issubclass(review.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
