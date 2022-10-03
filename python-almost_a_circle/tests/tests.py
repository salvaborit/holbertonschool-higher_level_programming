#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    # Test of Base() for assigning automatically an ID exists
    def test_base_id(self):
        b = Base()
        self.assertTrue(b.id)
