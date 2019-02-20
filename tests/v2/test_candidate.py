"""Test Class for candidate views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_candidate, create_office_v2, create_user, login_user, create_party_v2
from ..helper_data import CANDIDATE_DATA, OFFICE_DATA, USER_DATA, LOGIN_DATA, PARTY_DATA
from app.api.v2.models.candidate_model import Candidate
from app.database_config import init_db, destroydb


class TestCandidate(BaseTestCase):
    """docstring for TestCandidate"""
    destroydb()

    def setUp(self):
        super(TestCandidate, self).setUp()
        self.header = BaseTestCase.getHeader(self)

    def test_creating_a_candidate(self):
        """Test for creating a new candidate"""
        post = create_office_v2(self, OFFICE_DATA, self.header)
        response = create_party_v2(self, PARTY_DATA, self.header)
        resp = create_candidate(self, CANDIDATE_DATA, self.header)
        self.assertEqual(resp.json['data']['user'], 1)

        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
