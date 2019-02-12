"""Test Class for party views and model"""
import json
import unittest
import pdb
from .base_test import BaseTestCase
from .helper_methods import create_party
from .helper_data import PARTY_DATA, PARTY_EDITED_DATA
from app.api.v1.models.party_model import PoliticalParty


class TestParty(BaseTestCase):
    """docstring for TestParty"""

    def setUp(self):
        super(TestParty, self).setUp()

    def test_posting_a_party(self):
        """Test for creating a new party"""
        # PoliticalParty.political_parties.clear()
        resp = create_party(self, PARTY_DATA)
        # pdb.set_trace()
        self.assertEqual(resp.json['data'][0]['name'], 'ANC')
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_parties(self):
        """Test for getting all parties"""
        # PoliticalParty.political_parties.clear()
        resp = create_party(self, PARTY_DATA)
        # pdb.set_trace()
        resp = self.client.get(path='/api/v1/parties/')
        self.assertEqual(resp.json['data'][0]['name'], 'ANC')
        self.assertEqual(resp.status_code, 200)

    def test_deleting_a_party(self):
        """Test for deleting a party"""
        post = create_party(self, PARTY_DATA)
        int_id = int_id = int(post.json['data'][0]['id'])
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.delete(path, content_type='application/json')
        # pdb.set_trace()
        self.assertEqual(response.json['data'][0]['message'],
                         'Successfully deleted party with ID:{}'.format(int_id))
        self.assertEqual(response.status_code, 200)

    def test_getting_a_single_party(self):
        """Test for getting a single party"""
        resp = create_party(self, PARTY_DATA)
        # pdb.set_trace()
        int_id = int(resp.json['data'][0]['id'])
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        # pdb.set_trace()
        self.assertEqual(response.json['data']['name'], 'ANC')
        self.assertEqual(response.status_code, 200)

    def test_editing_a_party(self):
        """Test for editing a party"""
        resp = create_party(self, PARTY_DATA)
        int_id = int(resp.json['data'][0]['id'])
        # pdb.set_trace()
        path = '/api/v1/parties/{}'.format(int_id)
        response = self.client.put(path, data=json.dumps(
            PARTY_EDITED_DATA), content_type="application/json")
        # pdb.set_trace()
        self.assertEqual(response.json['data'][0]['name'], 'WIPER')
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            PoliticalParty.political_parties.clear()


if __name__ == '__main__':
    unittest.main()
