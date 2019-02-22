from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

office_id = 1
text = ""
evidence = ""
user_id = 1


class Petition(BaseModel):
    def __init__(self):
        pass

    def get_petitions(self):
        """method to get all petitions"""
        con = init_db()
        cur = con.cursor()
        query = "SELECT petition_id,office_id,user_id ,text,evidence from petition;"
        cur.execute(query)
        data = cur.fetchall()
        petition_list = []

        for i, items in enumerate(data):
            petition_id, office_id, user_id, text, evidence = items
            petition = dict(
                petition_id=petition_id,
                office_id=office_id,
                user_id=user_id,
                text=text,
                evidence=evidence
            )
            petition_list.append(petition)

        return dict(status=200, data=petition_list)

    def save_petition(self):
        petition = {
            "office_id": self.office_id,
            "user_id": self.user_id,
            "text": self.text,
            "evidence": self.evidence
        }
        # import pdb
        # pdb.set_trace()
        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO PETITION (office_id,user_id,text,evidence) VALUES \
             (%(office_id)s,%(user_id)s,%(text)s,%(evidence)s) Returning petition_id;"""
        cur.execute(query, petition)
        petition_id = cur.fetchone()[0]
        con.commit()
        con.close()
        petition_list = []
        petition_dict = dict(
            id=petition_id, text=petition['text'], office=petition['office_id'], createdBy=self.user_id, evidence=petition['evidence'])
        petition_list.append(petition_dict)
        success = {
            "status": 201,
            "data": petition_list

        }
        return success
