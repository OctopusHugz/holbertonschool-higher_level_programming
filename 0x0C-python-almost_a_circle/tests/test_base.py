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

    def test_pep8_adherence(self):
        """This function tests for adherence to pep8"""
        errors = 0
        f1 = pep8.Checker('tests/test_base.py')
        f2 = pep8.Checker('tests/test_rectangle.py')
        f3 = pep8.Checker('tests/test_square.py')
        f4 = pep8.Checker('models/base.py')
        f5 = pep8.Checker('models/rectangle.py')
        f6 = pep8.Checker('models/square.py')
        file_list = [f1, f2, f3, f4, f5, f6]
        for files in file_list:
            errors += files.check_all()
        self.assertEqual(errors, 0)


if __name__ == "__main__":
    unittest.main()
