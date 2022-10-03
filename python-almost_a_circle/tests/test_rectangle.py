#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests Rectangle instantiation"""

    def test_1a(self):
        """Regular instantiation with args(1, 2)"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)

    def test_1b(self):
        """Regular instantiation with args(1, 2, 3)"""
        self.r = Rectangle(1, 2, 3)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)

    def test_1c(self):
        """Regular instantiation with args(1, 2, 3, 4)"""
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_2a(self):
        """Invalid parameter type on instantiation"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
