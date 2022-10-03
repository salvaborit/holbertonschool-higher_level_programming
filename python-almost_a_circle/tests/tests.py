#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseIDs(unittest.TestCase):
    """Tests if ID attribute works correctly"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.id, 1)

    def test_2(self):
        self.assertEqual(self.b.id, 2)

    def test_3(self):
        self.assertEqual(self.b.id, 3)
