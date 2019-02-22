from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

user_id = 1
office_id = 1
party_id = 1


class Candidate(BaseModel):

    def __init__(self):
        pass
        # self.user_id = user_id
        # self.office_id = office_id
        # self.logoUrl = party_id

    def save_candidate(self):
        candidate = {
            "user_id": self.user_id,
            "office_id": self.office_id,
            "party_id": self.party_id

        }

        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO CANDIDATE (user_id,office_id,party_id) VALUES \
             (%(user_id)s,%(office_id)s,%(party_id)s);"""
        # bm = BaseModel()
        # if bm.check_exists('candidate', 'user_id', candidate['user_id']):
        #     return dict(status=409, error="Cannot register more than once")
        try:
            cur.execute(query, candidate)
        except Exception as e:
            return dict(status=403, error="Failed to create a candidate: " + str(e))

        # party_id = cur.fetchone()[0]
        con.commit()
        con.close()
        office_name = BaseModel.getFieldVal(
            self, 'office', 'name', 'office_id', self.office_id)
        candidate_name = BaseModel.getFieldVal(
            self, 'users', 'firstname', 'user_id', self.user_id)
        party_name = BaseModel.getFieldVal(
            self, 'party', 'name', 'party_id', self.party_id)
        success = {
            "status": 201,
            "data": {
                "office": self.office_id,
                "office_name": office_name,
                "user": self.user_id,
                "user_name": candidate_name,
                "party": self.party_id,
                "party_name": party_name
            }

        }
        return success

    def get_candidates(self):
        """method to get all candidates"""
        con = init_db()
        cur = con.cursor()
        query = "SELECT candidate_id,user_id, office_id ,party_id from candidate;"
        cur.execute(query)
        data = cur.fetchall()
        candidate_list = []

        for i, items in enumerate(data):
            candidate_id, user_id, office_id, party_id = items
            office_name = BaseModel.getFieldVal(
                self, 'office', 'name', 'office_id', office_id)
            candidate_name = BaseModel.getFieldVal(
                self, 'users', 'firstname', 'user_id', user_id)
            party_name = BaseModel.getFieldVal(
                self, 'party', 'name', 'party_id', party_id)
            candidate = dict(
                candidate_id=candidate_id,
                candidate_name=candidate_name,
                office_id=office_id,
                office_name=office_name,
                party_name=party_name
            )
            candidate_list.append(candidate)

        return dict(status=200, data=candidate_list)
