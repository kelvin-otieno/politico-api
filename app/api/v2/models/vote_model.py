from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

candidate_id = 1
office_id = 1
voter_id = 1
result = 0


class Vote(BaseModel):
    def __init__(self):
        pass
        # self.name = name.strip().lower()
        # self.hqAddress = hqAddress.strip().lower()
        # self.logoUrl = logoUrl.strip().lower()

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
        except:
            return dict(status=400, error="you can only vote once per office")

        # party_id = cur.fetchone()[0]
        con.commit()
        con.close()
        success = {
            "status": 201,
            "data": {
                "candidate": candidate_id,
                "voter": voter_id,
                "office_id": office_id
            }

        }
        return success

    # def count_votes(self, office_id):

    #     con = init_db()
    #     cur = con.cursor()

    #     query = "select * from vote where office_id = " + str(office_id)

    #     votes_list = []
    #     candidates_set = set()
    #     cur.execute(query)
    #     votes = cur.fetchall()
    #     for vote in votes:
    #         candidates_set.add(vote[1])
    #     result = 0
    #     for candidate in candidates_set:
    #         for vote in votes:
    #             if vote[1] == candidate:
    #                 result += 1
    #         votes_list.append(
    #             dict(office=office_id, candidate=candidate, result=result))

    #     con.commit()
    #     con.close()
    #     success = {
    #         "status": 200,
    #         "data": votes_list

    #     }
    #     return success
