from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request


class Vote(BaseModel):
    candidate_id = 1
    office_id = 1
    voter_id = 1
    result = 0

    def __init__(self):
        pass

    def cast_vote(self):
        vote = {
            "candidate_id": self.candidate_id,
            "office_id": self.office_id,
            "voter_id": self.voter_id

        }

        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO vote (candidate_id,voter_id,office_id) VALUES \
             (%(candidate_id)s,%(voter_id)s,%(office_id)s);"""
        bm = BaseModel()
        # if bm.check_exists('candidate', 'user_id', candidate['user_id']):
        #     return dict(status=409, error="Cannot register more than once")
        # try:

        # except:
        #     return dict(status=403, error="Forbidden. A candidate cannot be registered twice for the same office")
        # import pdb
        # pdb.set_trace()
        try:
            cur.execute(query, vote)
        except Exception as e:
            return dict(status=400, error=str(e))

        # party_id = cur.fetchone()[0]
        con.commit()
        con.close()
        user_id = BaseModel.getFieldVal(
            self, 'candidate', 'user_id', 'candidate_id', self.candidate_id)
        candidate_name = BaseModel.getFieldVal(
            self, 'users', 'firstname', 'user_id', user_id)
        voter_name = BaseModel.getFieldVal(
            self, 'users', 'firstname', 'user_id', self.voter_id)
        office_name = BaseModel.getFieldVal(
            self, 'office', 'name', 'office_id', self.office_id)
        success = {
            "status": 201,
            "data": {
                "candidate_id": self.candidate_id,
                "candidate_name": candidate_name,
                "voter_id": self.voter_id,
                "voter_name": voter_name,
                "office_id": self.office_id,
                "office_name": office_name
            }

        }
        return success

    def count_votes(self, office_id):

        con = init_db()
        cur = con.cursor()

        query = "select * from vote where office_id = " + str(office_id)

        votes_list = []
        candidates_set = set()
        cur.execute(query)
        votes = cur.fetchall()

        office_name = BaseModel.getFieldVal(
            self, 'office', 'name', 'office_id', office_id)
        for vote in votes:
            candidates_set.add(vote[1])

        for candidate in candidates_set:
            user_id = BaseModel.getFieldVal(
                self, 'candidate', 'user_id', 'candidate_id', candidate)
            candidate_name = BaseModel.getFieldVal(
                self, 'users', 'firstname', 'user_id', user_id)
            result = 0
            for vote in votes:
                if vote[1] == candidate:
                    result += 1
            votes_list.append(
                dict(office=office_id, of_name=office_name, candidate=candidate, cd_name=candidate_name, result=result))

        con.commit()
        con.close()
        success = {
            "status": 200,
            "data": votes_list

        }
        return success
