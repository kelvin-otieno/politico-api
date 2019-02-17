"""Test Class for office views and model"""
import unittest
from ..base_test import BaseTestCase
from ..helper_data import OFFICE_DATA
from ..helper_methods import create_office
from app.api.v1.models.office_model import PoliticalOffice


class TestOffice(BaseTestCase):
    """docstring for TestOffice"""

    def setUp(self):
        super(TestOffice, self).setUp()
        PoliticalOffice.political_offices.clear()

    def test_posting_an_office(self):
        """Test for creating a new office"""
        # PoliticalOffice.political_offices.clear()
        resp = create_office(self, OFFICE_DATA)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(resp.json['data'][0]['name'], 'MCA')
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_offices(self):
        """Test for getting all offfices"""
        # PoliticalOffice.political_offices.clear()
        response = create_office(self, OFFICE_DATA)
        # import pdb
        # pdb.set_trace()
        resp = self.client.get(path='/api/v1/offices/')
        self.assertEqual(len(resp.json['data']), 1)
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_office(self):
        """Test for getting a single office"""
        data = OFFICE_DATA
        post = create_office(self, data)
        # import pdb
        # pdb.set_trace()
        int_id = int(post.json['data'][0]['id'])
        path = '/api/v1/offices/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.json['data']['name'], 'MCA')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            PoliticalOffice.political_offices.clear()


if __name__ == '__main__':
    unittest.main()
