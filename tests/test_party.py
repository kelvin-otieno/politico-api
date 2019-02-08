"""Test Class for party views and model"""
import json
import unittest
from .base_test import BaseTestCase
from .helper_methods import create_party
from .helper_data import PARTY_DATA, PARTY_EDITED_DATA


class TestParty(BaseTestCase):
    """docstring for TestParty"""

    def setUp(self):
        super(TestParty, self).setUp()

    def test_posting_a_party(self):
        """Test for creating a new party"""
        resp = create_party(self, PARTY_DATA)
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_parties(self):
        """Test for getting all parties"""
        resp = self.client.get(path='/api/v1/parties/')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_party(self):
        """Test for getting a single party"""
        post = create_party(self, PARTY_DATA)
        int_id = int(post.json['data'][-1]['id'])
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_editing_a_party(self):
        """Test for editing a party"""
        post = create_party(self, PARTY_DATA)
        int_id = int(post.json['data'][-1]['id'])
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.put(
            path, data=json.dumps(PARTY_EDITED_DATA), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_party(self):
        """Test for deleting a party"""
        post = create_party(self, PARTY_DATA)
        int_id = int(post.json['data'][-1]['id'])
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
