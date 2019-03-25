"""Test Class for party views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_user, login_user
from ..helper_data import USER_DATA, LOGIN_DATA
from app.api.v2.models.user_model import User
from app.database_config import Database


class TestUser(BaseTestCase):
    """docstring for TestParty"""
    db = Database()
    db.destroydb()

    def setUp(self):
        super(TestUser, self).setUp()
        self.db.init_db()

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

    def test_getting_all_users(self):
        """Test for getting all users"""
        post = create_user(self, USER_DATA)
        resp = self.client.get(path='/api/v2/auth/')
        self.assertEqual(resp.json['data'][0]['email'], 'admin@admin.com')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_user(self):
        """Test for getting a user"""
        post = create_user(self, USER_DATA)
        resp = self.client.get(path='/api/v2/auth/1')
        self.assertEqual(resp.json['data'][0]['email'], 'admin@admin.com')
        self.assertEqual(resp.status_code, 200)

    def test_reset_password(self):
        """Test for resetting password"""
        header = BaseTestCase.getHeader(self)
        # post = create_user(self, USER_DATA)
        path = '/api/v2/auth/reset'
        response = self.client.post(
            path, data=json.dumps({"password": "password1", "token": header['token']}), content_type='application/json')
        self.assertEqual(response.json['data']
                         ['message'], 'password set successfully')

    def tearDown(self):
        with self.app.app_context():
            self.db.destroydb()


if __name__ == '__main__':
    unittest.main()
