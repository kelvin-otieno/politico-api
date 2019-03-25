"""Test Class for office views and model"""
import unittest
from ..base_test import BaseTestCase
from ..helper_data import OFFICE_DATA, USER_DATA, LOGIN_DATA, OFFICE_EDITED_DATA
from ..helper_methods import create_office_v2, create_user, login_user
from app.api.v2.models.office_model import PoliticalOffice
from app.database_config import Database
import json


class TestOffice(BaseTestCase):
    """docstring for TestOffice"""
    db = Database()
    db.destroydb()

    def setUp(self):
        super(TestOffice, self).setUp()
        self.header = BaseTestCase.getHeader(self)

    def test_posting_an_office(self):
        """Test for creating a new office"""
        resp = create_office_v2(self, OFFICE_DATA, self.header)
        self.assertEqual(resp.json['status'],
                         201)
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_offices(self):
        """Test for getting all offfices"""
        response = create_office_v2(self, OFFICE_DATA, self.header)
        resp = self.client.get(path='/api/v2/offices/', headers=self.header)
        self.assertEqual(resp.json['data'][0]['name'], 'mca')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_office(self):
        """Test for getting a single office"""
        data = OFFICE_DATA
        post = create_office_v2(self, data, self.header)
        path = '/api/v2/offices/1'
        response = self.client.get(
            path, content_type='application/json', headers=self.header)
        self.assertEqual(response.json['data'][0]['name'], 'mca')
        self.assertEqual(response.status_code, 200)

    def test_deleting_an_office(self):
        """Test for deleting an office"""
        data = OFFICE_DATA
        post = create_office_v2(self, data, self.header)
        path = '/api/v2/offices/1'
        response = self.client.delete(
            path, content_type='application/json', headers=self.header)
        self.assertEqual(response.json['message'],
                         'Office successfully deleted')
        self.assertEqual(response.status_code, 200)

    def test_editing_an_office(self):
        """Test for editing office"""
        resp = create_office_v2(self, OFFICE_DATA, self.header)
        path = '/api/v2/offices/1'
        response = self.client.put(path, data=json.dumps(
            OFFICE_EDITED_DATA), content_type="application/json", headers=self.header)
        self.assertEqual(response.json['message'], 'Changes made successfully')
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            self.db.destroydb()


if __name__ == '__main__':
    unittest.main()
