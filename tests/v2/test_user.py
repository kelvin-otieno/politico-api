"""Test Class for party views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_user, login_user
from ..helper_data import USER_DATA, LOGIN_DATA
from app.api.v2.models.user_model import User
from app.database_config import init_db, destroydb


class TestUser(BaseTestCase):
    """docstring for TestParty"""
    destroydb()

    def setUp(self):
        super(TestUser, self).setUp()
        init_db()

    def test_creating_a_user(self):
        """Test for creating a new user"""
        resp = create_user(self, USER_DATA)
        self.assertEqual(resp.json['message'],
                         'Successfully created user kelvin with ID:2')
        self.assertEqual(resp.status_code, 200)

    def test_login_user(self):
        """Test for login a user"""
        create_user(self, USER_DATA)
        resp = login_user(self, LOGIN_DATA)
        self.assertEqual(resp.json['data']['user']['firstname'], 'elsie')

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
