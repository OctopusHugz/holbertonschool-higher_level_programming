#!/usr/bin/python3
"""This module implements the TestSquare class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is an instance of the TestSquare class"""

    def test_square_id(self):
        """This function tests the setting of id attribute"""
        with self.assertRaises(TypeError):
            r1 = Square()
        with self.assertRaises(ValueError):
            r1 = Square(-42)


if __name__ == "__main__":
    unittest.main()
