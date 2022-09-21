#!/usr/bin/python3
"""Python interpreter"""


max_integer = __import__('6-max_integer').max_integer
import unittest

class TestMaxInteger(unittest.TestCase):
    """unittest for max integer"""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
