#!/usr/bin/env python3
"""
Unit tests for utils.py (nested map, get_json, memoize)
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Check it returns expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Check it raises KeyError for bad keys."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(expected_key))


class TestGetJson(unittest.TestCase):
    """Tests for get_json."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Check json is returned and request called once."""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator."""

    def test_memoize(self):
        """Check method runs once and then is cached."""

        class TestClass:
            """Simple class for memoize test."""

            def a_method(self):
                """Return a fixed number."""
                return 42

            @memoize
            def a_property(self):
                """Use a_method but cache result."""
                return self.a_method()

        with patch.object(
                TestClass, "a_method", return_value=42
                ) as mock_method:
            obj = TestClass()
            v1 = obj.a_property
            v2 = obj.a_property
            self.assertEqual(v1, 42)
            self.assertEqual(v2, 42)
            mock_method.assert_called_once()
