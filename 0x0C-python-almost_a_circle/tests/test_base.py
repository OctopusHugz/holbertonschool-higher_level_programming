#!/usr/bin/python3
"""This module implements the TestBase class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This is an instance of the TestBase class"""

    def test_base_id(self):
        """This function tests the setting of id attribute"""
        b1 = Base(42)
        self.assertEqual(b1.id, 42)
        b2 = Base(-42)
        self.assertEqual(b2.id, -42)
        b3 = Base()
        self.assertNotEqual(b3.id, 42)
        b4 = Base(None)
        self.assertNotEqual(b4.id, 42)


if __name__ == "__main__":
    unittest.main()
