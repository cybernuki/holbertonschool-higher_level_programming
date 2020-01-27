#!/usr/bin/python3
# Author: Jhonatan Arenas <1164@holbertonschool.com>
# tests/test_rectangle.py
"""This module contains a test case class for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    @classmethod
    def tearDownClass(self):
        print("\t[End of test_rectangle test cases]")
        setattr(Base, '_Base__nb_objects', 0)

    def test_instantiation_attributes(self):
        """Test for attributes of the instance"""
        r1 = Rectangle(10, 20)
        self.assertIsInstance(r1, Rectangle)

        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 20)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        self.assertAlmostEqual(r1.id, 1)
        
        r2 = Rectangle(20, 10)
        self.assertAlmostEqual(r2.width, 20)
        self.assertAlmostEqual(r2.height, 10)
        self.assertAlmostEqual(r2.x, 0)
        self.assertAlmostEqual(r2.y, 0)
        self.assertAlmostEqual(r2.id, 2)

        r1 = Rectangle(10, 20, 1, 2)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 20)
        self.assertAlmostEqual(r1.x, 1)
        self.assertAlmostEqual(r1.y, 2)
        self.assertAlmostEqual(r1.id, 3)

        r2 = Rectangle(10, 20, 2, 3)
        self.assertAlmostEqual(r2.width, 10)
        self.assertAlmostEqual(r2.height, 20)
        self.assertAlmostEqual(r2.x, 2)
        self.assertAlmostEqual(r2.y, 3)
        self.assertAlmostEqual(r2.id, 4)

        r1 = Rectangle(10, 20, 1, 2, 15)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 20)
        self.assertAlmostEqual(r1.x, 1)
        self.assertAlmostEqual(r1.y, 2)
        self.assertAlmostEqual(r1.id, 15)

        r2 = Rectangle(10, 20, 2, 3, 0)
        self.assertAlmostEqual(r2.width, 10)
        self.assertAlmostEqual(r2.height, 20)
        self.assertAlmostEqual(r2.x, 2)
        self.assertAlmostEqual(r2.y, 3)
        self.assertAlmostEqual(r2.id, 0)



