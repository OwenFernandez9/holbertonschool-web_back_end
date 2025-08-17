#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([("google",), ("abc",)])
    def test_org(self, org_name):
        expected = {"org": org_name}
        with patch("client.get_json") as mock_get_json:
            mock_get_json.return_value = expected

            client = GithubOrgClient(org_name)
            self.assertEqual(client.org, expected)

            mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org_name)
            )

if __name__ == "__main__":
    unittest.main()
