"""Test Class for party views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_party_v2, create_user, login_user
from ..helper_data import PARTY_DATA, PARTY_EDITED_DATA, USER_DATA, LOGIN_DATA
from app.api.v2.models.party_model import PoliticalParty
from app.database_config import init_db, destroydb


class TestParty(BaseTestCase):
    """docstring for TestParty"""
    destroydb()

    def setUp(self):
        super(TestParty, self).setUp()
        init_db()
        create_user(self, USER_DATA)
        response = login_user(self, LOGIN_DATA)
        token = response.json['data']['token']
        self.header = {'Content-Type': 'application/json', 'token': token}

    def test_posting_a_party(self):
        """Test for creating a new party"""
        resp = create_party_v2(self, PARTY_DATA, self.header)
        self.assertEqual(resp.json['status'], 201)
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_parties(self):
        """Test for getting all parties"""
        post = create_party_v2(self, PARTY_DATA, self.header)
        resp = self.client.get(path='/api/v2/parties/', headers=self.header)
        self.assertEqual(resp.json['data'][0]['name'], 'anc')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_party(self):
        """Test for getting all parties"""
        resp = create_party_v2(self, PARTY_DATA, self.header)
        resp = self.client.get(path='/api/v2/parties/1', headers=self.header)
        self.assertEqual(resp.json['data'][0]['name'], 'anc')
        self.assertEqual(resp.status_code, 200)

    def test_deleting_a_party(self):
        """Test for deleting a party"""
        post = create_party_v2(self, PARTY_DATA, self.header)
        path = '/api/v2/parties/1'
        response = self.client.delete(
            path, content_type='application/json', headers=self.header)
        self.assertEqual(response.json['message'],
                         'Party successfully deleted')
        self.assertEqual(response.status_code, 200)

    def test_editing_a_party(self):
        """Test for editing a party"""
        resp = create_party_v2(self, PARTY_DATA, self.header)
        path = '/api/v2/parties/1'
        response = self.client.patch(path, data=json.dumps(
            PARTY_EDITED_DATA), content_type="application/json", headers=self.header)
        self.assertEqual(response.json['message'], 'Changes made successfully')
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
