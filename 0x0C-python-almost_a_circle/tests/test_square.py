#!/usr/bin/python3
"""This module implements the TestSquare class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is an instance of the TestSquare class"""

    def test_square_instantiation(self):
        """This function tests the setting of id attribute"""
        s1 = Square(42)
        self.assertEqual(s1.size, 42)

        s2 = Square(42, 13, 22, 98)
        self.assertEqual(s2.x, 13)
        self.assertEqual(s2.y, 22)
        self.assertEqual(s2.id, 98)
        self.assertEqual(s2.__str__(), "[Square] (98) 13/22 - 42")

        s3 = Square(42, 13, 22, -98)
        self.assertEqual(s3.id, -98)
        self.assertEqual(s3.area(), 1764)

        s4 = Square(1, 1, 1, 1)
        s4.update(13, 22, 42, 98)
        self.assertEqual(s4.id, 13)
        self.assertEqual(s4.size, 22)
        self.assertEqual(s4.x, 42)
        self.assertEqual(s4.y, 98)

        s5 = Square(1, 1, 1, 1)
        s5.update(y=98, size=22, id=13,  x=42)
        self.assertEqual(s5.id, 13)
        self.assertEqual(s5.size, 22)
        self.assertEqual(s5.x, 42)
        self.assertEqual(s5.y, 98)

        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(TypeError):
            s1 = Square("holbie")
        with self.assertRaises(TypeError):
            s1 = Square(42, "holbie")
        with self.assertRaises(TypeError):
            s1 = Square(42, 98, "holbie")

        with self.assertRaises(ValueError):
            s1 = Square(-42)
        with self.assertRaises(ValueError):
            s1 = Square(42, -98)
        with self.assertRaises(ValueError):
            s1 = Square(42, 98, -13)


if __name__ == "__main__":
    unittest.main()
