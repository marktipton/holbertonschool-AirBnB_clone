#!/usr/bin/python3
"""unittests for Amenity"""
import unittest
import pep8
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

    def test_init(self):
        """test base constructor"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_save(self):
        """test save method"""
        amenity = Amenity()
        before_update = amenity.updated_at
        amenity.save()
        self.assertNotEqual(before_update, amenity.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        amenity = Amenity()
        inst_dict = amenity.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "Amenity")
        self.assertEqual(
            inst_dict["created_at"], amenity.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], amenity.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        amenity = Amenity()
        str_rep = str(amenity)
        self.assertIn(f"[Amenity] ({amenity.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = Amenity()
        base_2 = Amenity()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = Amenity(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = Amenity(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = Amenity()
        serialized_data = base_1.to_dict()
        deserialized_base = Amenity(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
