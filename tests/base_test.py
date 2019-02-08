"""Base Test Class"""
import unittest
from run import app


class BaseTestCase(unittest.TestCase):
    """This is the base test for our app. Contains methods that will often be used in other tests"""

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
