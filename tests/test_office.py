"""Test Class for party views and model"""
import unittest
from .base_test import BaseTestCase
from .helper_data import OFFICE_DATA
from .helper_methods import create_office


class TestOffice(BaseTestCase):
    """docstring for TestParty"""

    def setUp(self):
        super(TestOffice, self).setUp()

    def test_posting_an_office(self):
        """Test for creating a new office"""
        resp = create_office(self, OFFICE_DATA)
        self.assertEqual(resp.status_code, 200)

    def test_getting_all_offices(self):
        """Test for getting all offfices"""
        resp = self.client.get(path='/api/v1/offices/')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_office(self):
        """Test for getting a single office"""
        data = OFFICE_DATA
        post = create_office(self, data)
        int_id = int(post.json['data'][-1]['id'])
        path = '/api/v1/offices/{}'.format(int_id)
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
