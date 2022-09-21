#!/usr/bin/python3
"""Python interpreter"""


max_integer = __import__('6-max_integer').max_integer
import unittest

class TestMaxInteger(unittest.TestCase):
    """unittest for max integer"""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_start(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_elem_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), "")
