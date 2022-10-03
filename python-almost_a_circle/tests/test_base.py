#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.base import Base


class TestBaseID(unittest.TestCase):
    """Tests ID attribute"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.id, 1)

    def test_2(self):
        self.assertEqual(self.b.id, 2)

    def test_3(self):
        self.assertEqual(self.b.id, 3)

class TestBaseID89(unittest.TestCase):
    """Tests for ID assignment"""

    def test_1(self):
        self.b = Base(89)
        self.assertEqual(self.b.id, 89)

class TestToJsonString(unittest.TestCase):
    """Tests to_json_string() method"""

    def setUp(self):
        self.b = Base()

    def test_1(self):
        self.assertEqual(self.b.to_json_string(None), "[]")

    def test_1(self):
        # empty_list = []
        self.assertEqual(self.b.to_json_string([]), "[]")
