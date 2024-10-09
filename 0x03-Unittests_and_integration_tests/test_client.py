#!/usr/bin/env python3
''' A module with a test class TestGithubOrgClient '''

import client
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    ''' A class to test the client.GithubOrgClient class '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])

    @patch('client.get_json')    # we're mocking this method
    def test_org(self, org_name, mock_client):
        ''' Test that GithubOrgClient.org returns the correct value '''

        url = f'https://api.github.com/orgs/{org_name}'
        test = GithubOrgClient(org_name)
        test.org()	# calling the method that'll trigger get_json
        
        mock_client.assert_called_once_with(url)

    @parameterized.expand([
        ('google'),
        ('abc')
    ])

    def test_public_repos_url(self, org_name):
        # unit-test GithubOrgClient._public_repos_url

        with patch.object(GithubOrgClient, '_public_repos_url') as mock_patch:
            test = GithubOrgClient(org_name)
            payload = {'repos_url': f'https://api.github.com/orgs/{org_name}'}
            mock_patch.return_value = payload
            result = test._public_repos_url()
            self.assertEqual(result, payload)
