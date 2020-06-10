#!/usr/bin/python3
"""This module implements the TestSquare class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is an instance of the TestSquare class"""

    def test_square_instantiation(self):
        """This function tests the setting of id attribute"""
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(TypeError):
            s1 = Square("holbie")

        with self.assertRaises(ValueError):
            s1 = Square(-42)

        s1 = Square(42)
        self.assertEqual(s1.size, 42)
        s2 = Square(42, 13, 22, 98)
        self.assertEqual(s2.x, 13)
        self.assertEqual(s2.y, 22)
        self.assertEqual(s2.id, 98)
        self.assertEqual(s2.__str__(), "[Square] (98) 13/22 - 42")


if __name__ == "__main__":
    unittest.main()
