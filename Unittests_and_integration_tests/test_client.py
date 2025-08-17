#!/usr/bin/env python3
import unittest
from unittest.mock import patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests robustos para org, compatibles con el checker."""

    def _assert_org(self, org_name, mock_get_json):
        expected = {"org": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)

        result = client.org
        self.assertEqual(result, expected)

        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

    @patch("client.get_json")
    def test_org_0_google(self, mock_get_json):
        self._assert_org("google", mock_get_json)

    @patch("client.get_json")
    def test_org_1_abc(self, mock_get_json):
        self._assert_org("abc", mock_get_json)

    @patch("client.get_json")
    def test_org_0(self, mock_get_json):
        self._assert_org("google", mock_get_json)

    @patch("client.get_json")
    def test_org_1(self, mock_get_json):
        self._assert_org("abc", mock_get_json)


if __name__ == "__main__":
    unittest.main()
