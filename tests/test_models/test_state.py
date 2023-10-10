#!/usr/bin/python3
"""unittests for State"""
import unittest
import pep8
from models.state import State
from datetime import datetime


class TestStateDoc(unittest.TestCase):
    """check FileStorage documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(State.__doc__) > 0)


class TestStatePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/state.py'
            'tests/test_models/test_state.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


class TestState(unittest.TestCase):
    """tests for State"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_save(self):
        """test save method"""
        state = State()
        before_update = state.updated_at
        state.save()
        self.assertNotEqual(before_update, state.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        state = State()
        inst_dict = state.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "State")
        self.assertEqual(
            inst_dict["created_at"], state.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], state.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        state = State()
        str_rep = str(state)
        self.assertIn(f"[State] ({state.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = State()
        base_2 = State()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = State(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = State(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = State()
        serialized_data = base_1.to_dict()
        deserialized_base = State(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
