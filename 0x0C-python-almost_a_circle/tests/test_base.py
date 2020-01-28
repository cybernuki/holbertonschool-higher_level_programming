#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# test/test_base.py
"""This module contains test cases for a Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    @classmethod
    def setUpClass(self):
        print("[Start of Base Test cases]")

    @classmethod
    def tearDownClass(self):
        print("\Done")

    def test_instantiation(self):
        """Checouts id manager and instantaion"""
        self.assertAlmostEqual(self.b1.id, 1)
        self.assertAlmostEqual(self.b2.id, 2)
        self.assertAlmostEqual(self.b3.id, 3)
        self.assertAlmostEqual(self.b4.id, 12)
        self.assertAlmostEqual(self.b5.id, 4)

        self.assertIsInstance(self.b1, Base)
        self.assertIsInstance(self.b2, Base)
        self.assertIsInstance(self.b3, Base)
        self.assertIsInstance(self.b4, Base)
        self.assertIsInstance(self.b5, Base)


if __name__ == "__main__":
    unittest.main()
