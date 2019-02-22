"""Test Class for votes views and model"""
import json
import unittest
import pdb
from ..base_test import BaseTestCase
from ..helper_methods import create_candidate, create_office_v2, create_user, create_vote, login_user, create_party_v2
from ..helper_data import CANDIDATE_DATA, OFFICE_DATA, USER_DATA, VOTING_DATA, PARTY_DATA, LOGIN_DATA
from app.api.v2.models.vote_model import Vote
from app.database_config import init_db, destroydb


class TestVote(BaseTestCase):
    """docstring for TestVote"""
    destroydb()

    def setUp(self):
        super(TestVote, self).setUp()
        self.header = BaseTestCase.getHeader(self)

    def test_voting(self):
        """Test for casting a vote"""
        create_office_v2(self, OFFICE_DATA, self.header)
        create_party_v2(self, PARTY_DATA, self.header)
        create_candidate(self, CANDIDATE_DATA, self.header)
        resp = create_vote(self, VOTING_DATA, self.header)
        self.assertEqual(resp.json['data']['candidate_id'], 1)
        self.assertEqual(resp.status_code, 200)

    def test_vote_counting(self):
        """Test for counting votes"""
        create_office_v2(self, OFFICE_DATA, self.header)
        create_party_v2(self, PARTY_DATA, self.header)
        create_candidate(self, CANDIDATE_DATA, self.header)
        create_vote(self, VOTING_DATA, self.header)
        response = self.client.get(path='/api/v2/office/1/result/')
        self.assertEqual(response.json['data'][0]['result'], 1)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            destroydb()


if __name__ == '__main__':
    unittest.main()
