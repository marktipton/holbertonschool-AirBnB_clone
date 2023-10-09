#!/usr/bin/python3
"""unittests for Place"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """tests for Place"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_save(self):
        """test save method"""
        place = Place()
        before_update = place.updated_at
        place.save()
        self.assertNotEqual(before_update, place.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        place = Place()
        inst_dict = place.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "Place")
        self.assertEqual(
            inst_dict["created_at"], place.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], place.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        place = Place()
        str_rep = str(place)
        self.assertIn(f"[Place] ({place.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = Place()
        base_2 = Place()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = Place(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = Place(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = Place()
        serialized_data = base_1.to_dict()
        deserialized_base = Place(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
