"""Base Test Class"""
import unittest
from run import app
from .helper_methods import create_user, login_user
from .helper_data import USER_DATA, LOGIN_DATA
from app.database_config import Database


class BaseTestCase(unittest.TestCase):
    """This is the base test for our app. Contains methods that will often be used in other tests"""

    db = Database()

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def getHeader(self):
        us = create_user(self, USER_DATA)
        response = login_user(self, LOGIN_DATA)
        token = response.json['data']['token']
        self.header = {'Content-Type': 'application/json', 'token': token}
        return self.header
