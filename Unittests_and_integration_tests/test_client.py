#!/usr/bin/env python3
import sys
import types
import unittest
from unittest.mock import patch
from parameterized import parameterized

if 'requests' not in sys.modules:
    sys.modules['requests'] = types.SimpleNamespace(get=lambda *a, **k: None)

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        expected = {"org": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)

        result = client.org
        self.assertEqual(result, expected)

        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )


if __name__ == "__main__":
    unittest.main()
