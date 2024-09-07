#!/usr/bin/env python3
"""A module to perform unittesting"""
import unittest
from parameterized import parameterized
import utils
from typing import Mapping, List, Union


class TestAccessNestedMap(unittest.TestCase):
    """ class to test the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, data: Mapping, path: List[str],
                               expected: Union[int, Mapping]) -> None:
        """ unit test for utils.access_nested_map """
        self.assertEqual(utils.access_nested_map(data, path), expected)
