#!/usr/bin/python3
"""This module implements the TestRectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This is an instance of the TestRectangle class"""

    def test_rectangle_id(self):
        """This function tests the setting of id attribute"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(42)
        with self.assertRaises(TypeError):
            r2 = Rectangle(-42)
        with self.assertRaises(TypeError):
            r2 = Rectangle(None)


if __name__ == "__main__":
    unittest.main()
