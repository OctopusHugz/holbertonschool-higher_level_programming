#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class implements test case instances for testing max integer"""

    def test_type(self):
        """This function tests the type of elements for intness"""
        with self.assertRaises(TypeError):
            max_integer([1, "holbie", 2, 3, 4])

    def test_return(self):
        """This function tests the return values from the function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([11, 23, 34, 42]), 42)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
