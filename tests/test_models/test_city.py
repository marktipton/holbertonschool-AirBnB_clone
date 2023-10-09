#!/usr/bin/python3
"""unittests for City"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """tests for City"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_save(self):
        """test save method"""
        city = City()
        before_update = city.updated_at
        city.save()
        self.assertNotEqual(before_update, city.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        city = City()
        inst_dict = city.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "City")
        self.assertEqual(
            inst_dict["created_at"], city.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], city.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        city = City()
        str_rep = str(city)
        self.assertIn(f"[City] ({city.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = City()
        base_2 = City()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = City(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = City(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = City()
        serialized_data = base_1.to_dict()
        deserialized_base = City(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
