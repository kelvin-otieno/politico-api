"""Test Class for party views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_party_v2
from ..helper_data import PARTY_DATA, PARTY_EDITED_DATA
from app.api.v2.models.party_model import PoliticalParty
from app.database_config import init_db, destroydb


class TestParty(BaseTestCase):
    """docstring for TestParty"""
    destroydb()

    def setUp(self):
        super(TestParty, self).setUp()
        init_db()

    def test_posting_a_party(self):
        """Test for creating a new party"""
        resp = create_party_v2(self, PARTY_DATA)
        self.assertEqual(resp.json['status'], 201)
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_parties(self):
        """Test for getting all parties"""
        resp = create_party_v2(self, PARTY_DATA)
        resp = self.client.get(path='/api/v2/parties/')
        self.assertEqual(resp.json['data'][0]['name'], 'anc')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_party(self):
        """Test for getting all parties"""
        resp = create_party_v2(self, PARTY_DATA)
        resp = self.client.get(path='/api/v2/parties/1')
        self.assertEqual(resp.json['data'][0]['name'], 'anc')
        self.assertEqual(resp.status_code, 200)

    def test_deleting_a_party(self):
        """Test for deleting a party"""
        post = create_party_v2(self, PARTY_DATA)
        path = '/api/v2/parties/1'
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.json['message'],
                         'Party successfully deleted')
        self.assertEqual(response.status_code, 200)

    def test_editing_a_party(self):
        """Test for editing a party"""
        resp = create_party_v2(self, PARTY_DATA)
        path = '/api/v2/parties/1'
        response = self.client.put(path, data=json.dumps(
            PARTY_EDITED_DATA), content_type="application/json")
        self.assertEqual(response.json['message'], 'Changes made successfully')
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
