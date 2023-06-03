#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_empty_list(self):
        a = []
        self.assertIsNone(max_integer(a))

    def test_list_with_one_item(self):
        max = max_integer([8])
        self.assertEqual(max, 8)

    def test_no_arg(self):
        max = max_integer()
        self.assertIsNone(max)

    def test_normal_list(self):
        max = max_integer([4, 5, 78, 90, 100])
        self.assertEqual(max, 100)

    def test_negative_values(self):
        max = max_integer([-4, -5, -78, -9, -100])
        self.assertEqual(max, -4)

    def test_middle_negative_value(self):
        max = max_integer([4, 5, -78, 90, 10])
        self.assertEqual(max, 90)

    def test_middle(self):
        max = max_integer([4, 5, 78, 65, 77])
        self.assertEqual(max, 78)

    def test_beginning(self):
        max = max_integer([47, 5, 34, 24, 7])
        self.assertEqual(max, 47)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

