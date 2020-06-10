#!/usr/bin/python3
"""This module implements the TestRectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This is an instance of the TestRectangle class"""

    def test_rectangle_instantiation(self):
        """This function tests the setting of id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(10, 2, 42, 98, 12)
        self.assertEqual(r3.x, 42)
        self.assertEqual(r3.y, 98)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.__str__(), "[Rectangle] (12) 42/98 - 10/2")

        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(42)
        with self.assertRaises(TypeError):
            r1 = Rectangle(-42)
        with self.assertRaises(TypeError):
            r1 = Rectangle(None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(42, "holbie")
        with self.assertRaises(TypeError):
            r1 = Rectangle("holbie", 98)
        with self.assertRaises(TypeError):
            r1 = Rectangle(42, 98, "holbie", 0)
        with self.assertRaises(TypeError):
            r1 = Rectangle(42, 98, 0, "holbie")

        with self.assertRaises(ValueError):
            r1 = Rectangle(-42, 98)
        with self.assertRaises(ValueError):
            r1 = Rectangle(42, -98)
        with self.assertRaises(ValueError):
            r1 = Rectangle(42, 98, -1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(42, -98, 0, -1)


if __name__ == "__main__":
    unittest.main()
