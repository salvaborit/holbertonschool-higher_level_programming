#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests Rectangle instantiation"""

    def test_1(self):
        """Test for regular instantiation"""
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_2(self):
        """Test for wrong parameters on instantiation"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
