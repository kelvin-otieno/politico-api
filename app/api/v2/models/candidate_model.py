from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

user_id = 1
office_id = 1


class Candidate(BaseModel):
    def __init__(self):
        pass
        # self.name = name.strip().lower()
        # self.hqAddress = hqAddress.strip().lower()
        # self.logoUrl = logoUrl.strip().lower()

    def save_candidate(self):
        candidate = {
            "user_id": self.user_id,
            "office_id": self.office_id

        }

        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO CANDIDATE (user_id,office_id) VALUES \
             (%(user_id)s,%(office_id)s);"""
        bm = BaseModel()
        if bm.check_exists('candidate', 'user_id', candidate['user_id']):
            return dict(status=409, error="Cannot register more than once")
        try:
            cur.execute(query, candidate)
        except:
            return dict(status=403, error="Forbidden. A candidate cannot be registered twice for the same office")

        # party_id = cur.fetchone()[0]
        con.commit()
        con.close()
        success = {
            "status": 201,
            "data": {
                "office": office_id,
                "user": user_id
            }

        }
        return success
