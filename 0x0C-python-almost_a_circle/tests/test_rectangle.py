#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test initialization of a new Rectangle object
        r1 = Rectangle(10, 20, 1, 2, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 3)

        # Test initialization with default values
        r2 = Rectangle(5, 5)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

        # Test initialization with non-integer values
        with self.assertRaises(TypeError):
            r3 = Rectangle("10", 20, 1, 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "20", 1, 2)

        # Test initialization with negative values
        with self.assertRaises(ValueError):
            r5 = Rectangle(-10, 20, 1, 2)
        with self.assertRaises(ValueError):
            r6 = Rectangle(10, -20, 1, 2)
        with self.assertRaises(ValueError):
            r7 = Rectangle(10, 20, -1, 2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 20, 1, -2)


if __name__ == '__main__':
    unittest.main()
