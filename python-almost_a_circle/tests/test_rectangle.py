#!/usr/bin/python3
"""Python interpreter"""


from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class TestRectInstantiation(unittest.TestCase):
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


class TestRectMethods(unittest.TestCase):
    def test_area(self):
        """Area method"""
        self.r = Rectangle(1, 2)
        self.assertEqual(self.r.area(), 2)

    def test__str__(self):
        """___str___ method"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_display(self):
        """display() method"""
        stdout = StringIO()
        sys.stdout = stdout
        r = Rectangle(2, 1, 0, 0)
        r.display()
        self.assertEqual(stdout.getvalue(), '##\n')

        stdout = StringIO()
        sys.stdout = stdout
        r = Rectangle(2, 1, 1, 0)
        r.display()
        self.assertEqual(stdout.getvalue(), ' ##\n')

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

    def test_create(self):
        """create() method"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)


class TestRectSave1(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file1(self):
        """save_to_file() method"""
        Rectangle.save_to_file(None)
        with open('Rectangle.json') as file:
            self.assertEqual('[]', file.read())


class TestRectSave2(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file2(self):
        """save_to_file() method"""
        Rectangle.save_to_file([])
        with open('Rectangle.json') as file:
            self.assertEqual('[]', file.read())


class TestRectSave3(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file3(self):
        """save_to_file() method"""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open('Rectangle.json') as file:
            self.assertEqual(
                '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]', file.read())
