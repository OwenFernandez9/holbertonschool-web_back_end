#!/usr/bin/env python3
"""
Unit tests and integration tests for client.py (GithubOrgClient).
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


def _idx_only_name(func, num, params_dict):
    """Helper for parameterized to force test names with only the index."""
    return f"{func.__name__}_{num}"


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient methods (unit level)."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Ensure .org returns the expected payload and calls get_json once."""
        expected = {"org": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

    def test_public_repos_url(self):
        """Ensure _public_repos_url matches repos_url from the mocked org payload."""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Ensure public_repos returns only repo names and calls mocks once."""
        repos_api_url = "https://api.github.com/orgs/google/repos"
        payload = [
            {"name": "repo-uno"},
            {"name": "repo-dos"},
            {"name": "repo-tres"},
        ]
        mock_get_json.return_value = payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = repos_api_url

            client = GithubOrgClient("google")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo-uno", "repo-dos", "repo-tres"])
            self.assertEqual(mock_repos_url.call_count, 1)
            mock_get_json.assert_called_once_with(repos_api_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ], name_func=_idx_only_name)
    def test_has_license(self, repo, license_key, expected):
        """Ensure has_license returns the expected boolean."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests:
    - Mock only requests.get
    - Use real utils.get_json
    - Drive responses via fixtures based on requested URL
    """

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and route responses by URL."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        org_url = GithubOrgClient.ORG_URL.format(org="google")
        repos_url = cls.org_payload["repos_url"]

        def side_effect(url, *args, **kwargs):
            resp = Mock()
            if url == org_url:
                resp.json.return_value = cls.org_payload
            elif url == repos_url:
                resp.json.return_value = cls.repos_payload
            else:
                resp.json.return_value = {}
            return resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_apache2(self):
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
