#!/usr/bin/env python3
"""A module to perform unittesting"""
import unittest
from parameterized import parameterized
import utils
from unittest.mock import patch
from typing import Mapping, List, Union, Type, Dict


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

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, data: Mapping, path: List[str],
                                         expected: Type[Exception]) -> None:
        """ raise KeyError if wrong input is entered """
        with self.assertRaises(expected):
            utils.access_nested_map(data, path)


class TestGetJson(unittest.TestCase):
    ''' Implement the test_get_json method '''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Mapping[str, bool]) -> None:
        ''' test that utils.get_json returns the expected result. '''
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload

            # Call assert to check if the request works
            self.assertEqual(utils.get_json(test_url), test_payload)

            # assert that the mock was executed atleast once when called
            mock.assert_called_once_with(test_url)
