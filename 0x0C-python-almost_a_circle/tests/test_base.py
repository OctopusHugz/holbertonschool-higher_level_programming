#!/usr/bin/python3
"""This module implements the TestBase class"""
import unittest
import pep8
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

    def test_pep8(self):
        """This function tests for pep8 conformance"""
        p8s = pep8.StyleGuide(quiet=True)
        error_check = p8s.check_files(
            ['test_base.py', 'test_rectangle.py', 'test_square.py',
             '../models/base.py', '../models/rectangle.py',
             '../models/square.py'])
        self.assertEqual(error_check.total_errors, 6)


if __name__ == "__main__":
    unittest.main()
