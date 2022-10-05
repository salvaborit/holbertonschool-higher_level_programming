#!/usr/bin/python3
"""Python interpreter"""


import unittest
from models.square import Square


class TestSqInstantiation(unittest.TestCase):
    """Instantiation"""

    def test_regular_instantiation_1(self):
        """Regular instantiation"""
        self.s = Square(1)
        self.assertEqual(self.s.size, 1)
        self.s = Square(1, 2)
        self.assertEqual(self.s.x, 2)
        self.s = Square(1, 2, 3)
        self.assertEqual(self.s.y, 3)
        self.s = Square(1, 2, 3, 4)
        self.assertEqual(self.s.id, 4)

    def test_invalid_arg_type(self):
        """Invalid argument type on instantiation"""
        self.assertRaises(TypeError, Square, "1", 2)
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)


class TestSqMethods(unittest.TestCase):
    """Methods"""

    def test__str__(self):
        """__str__() method"""
        self.s = Square(1, 2, 3, 4)
        self.assertEqual(self.s.__str__(), '[Square] (4) 2/3 - 1')

    def test_to_dictionary(self):
        """to_dictionary() method"""
        self.s = Square(1, 2, 3, 4)
        self.assertEqual(self.s.to_dictionary(), {
                         'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update_int_arguments(self):
        """update() method with regular integer arguments passed"""
        self.s = Square(10, 10, 10, 10)
        self.s.update()
        self.assertEqual(self.s.to_dictionary(), {
                         'id': 10, 'size': 10, 'x': 10, 'y': 10})
        self.s.update(89)
        self.assertEqual(self.s.id, 89)
        self.s.update(89, 1)
        self.assertEqual(self.s.width, 1)
        self.s.update(89, 1, 2)
        self.assertEqual(self.s.x, 2)
        self.s.update(89, 1, 2, 3)
        self.assertEqual(self.s.y, 3)

    def test_update_dict_arguments(self):
        """update() method with dictionary type
        (**, key='value') argument passed"""
        self.s = Square(10, 10, 10, 10)
        self.s.update(**{'id': 89})
        self.assertEqual(self.s.id, 89)
        self.s.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.s.width, 1)
        self.s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.s.x, 2)
        self.s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.s.y, 3)

    def test_create(self):
        """create() method"""
        self.s = Square.create(**{'id': 89})
        self.assertEqual(self.s.id, 89)
        self.s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(self.s.width, 1)
        self.s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.s.x, 2)
        self.s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.s.y, 3)


class TestSqSave1(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file1(self):
        """save_to_file() method"""
        Square.save_to_file(None)
        with open('Square.json') as file:
            self.assertEqual('[]', file.read())


class TestSqSave2(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file2(self):
        """save_to_file() method"""
        empty_list = []
        # filename = 'Square.json'
        Square.save_to_file(empty_list)
        with open('Square.json') as file:
            self.assertEqual('[]', file.read())


class TestSqSave3(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file3(self):
        """save_to_file() method"""
        Square.save_to_file([Square(1, 0, 0, 1)])
        with open('Square.json') as file:
            self.assertEqual(
                '[{"id": 1, "size": 1, "x": 0, "y": 0}]', file.read())


class TestSqLoad(unittest.TestCase):
    """load_from_file() method"""

    def test_load_from_file(self):
        """load_from_file() method"""
        Square.save_to_file([Square(1, 2)])
        lf = Square.load_from_file()
        self.assertTrue(isinstance(lf, list))


if __name__ == '__main__':
    unittest.main()
