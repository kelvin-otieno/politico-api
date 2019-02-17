"""Test Class for office views and model"""
import unittest
from ..base_test import BaseTestCase
from ..helper_data import OFFICE_DATA
from ..helper_methods import create_office_v2
from app.api.v2.models.office_model import PoliticalOffice
from app.database_config import init_db, destroydb


class TestOffice(BaseTestCase):
    """docstring for TestOffice"""

    destroydb()

    def setUp(self):
        super(TestOffice, self).setUp()
        init_db()

    def test_posting_an_office(self):
        """Test for creating a new office"""
        resp = create_office_v2(self, OFFICE_DATA)
        self.assertEqual(resp.json['message'],
                         'Successfully created mca office with ID:1')
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_offices(self):
        """Test for getting all offfices"""
        response = create_office_v2(self, OFFICE_DATA)
        resp = self.client.get(path='/api/v2/offices/')
        self.assertEqual(resp.json['data'][0]['name'], 'mca')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_office(self):
        """Test for getting a single office"""
        data = OFFICE_DATA
        post = create_office_v2(self, data)
        path = '/api/v2/offices/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.json['data'][0]['name'], 'mca')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
