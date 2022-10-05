#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.rectangle import Rectangle


class TestInstantiation(unittest.TestCase):
    """Instantiation"""

    def test_regular_instantiation_1(self):
        """Regular instantiation with args(1, 2)"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)

    def test_regular_instantiation_2(self):
        """Regular instantiation with args(1, 2, 3)"""
        self.r = Rectangle(1, 2, 3)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)

    def test_regular_instantiation_3(self):
        """Regular instantiation with args(1, 2, 3, 4)"""
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_regular_instantiation_4(self):
        """Regular instantiation with args(1, 2, 3, 4, 5)"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)

    def test_invalid_arg_type(self):
        """Invalid argument type on instantiation"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_instantiation_with_negatives_zero(self):
        """Instantiation with negatives/zero"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)


class TestMethods(unittest.TestCase):
    def test_area(self):
        """Area method"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.area(), 2)

    def test__str__(self):
        """___str___ method"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_to_dict(self):
        """to_dictionary() method"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.to_dictionary(), {
                         'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update_nothing(self):
        """update() method with no args"""
        self.r1 = Rectangle(1, 2, 3, 4, 5)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.r2.update()
        self.assertEqual(self.r1.to_dictionary(), self.r2.to_dictionary())

    def test_update_int_arguments(self):
        """update() method with regular integer arguments passed"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.r.update(89)
        self.assertEqual(self.r.id, 89)
        self.r.update(89, 1)
        self.assertEqual(self.r.width, 1)
        self.r.update(89, 1, 2)
        self.assertEqual(self.r.height, 2)
        self.r.update(89, 1, 2, 3)
        self.assertEqual(self.r.x, 3)
        self.r.update(89, 1, 2, 3, 4)
        self.assertEqual(self.r.y, 4)

    def test_update_dict_arguments(self):
        """update() method with dictionary type
        (**, key='value') argument passed"""
        self.r = Rectangle(10, 10, 10, 10, 10)
        self.r.update(**{'id': 89})
        self.assertEqual(self.r.id, 89)
        self.r.update(**{'id': 89, 'width': 1})
        self.assertEqual(self.r.width, 1)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(self.r.height, 2)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(self.r.x, 3)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(self.r.y, 4)
