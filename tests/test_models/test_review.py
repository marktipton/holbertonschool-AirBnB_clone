#!/usr/bin/python3
"""unittests for Review"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """tests for Review"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_save(self):
        """test save method"""
        review = Review()
        before_update = review.updated_at
        review.save()
        self.assertNotEqual(before_update, review.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        review = Review()
        inst_dict = review.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "Review")
        self.assertEqual(
            inst_dict["created_at"], review.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], review.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        review = Review()
        str_rep = str(review)
        self.assertIn(f"[Review] ({review.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = Review()
        base_2 = Review()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = Review(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = Review(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = Review()
        serialized_data = base_1.to_dict()
        deserialized_base = Review(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
