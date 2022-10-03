#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests Rectangle instantiation"""

    def test_1(self):
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
