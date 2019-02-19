from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

name = ""
hqAddress = ""
logoUrl = ""


class PoliticalParty(BaseModel):
    def __init__(self):
        pass
        self.name = name.strip().lower()
        self.hqAddress = hqAddress.strip().lower()
        self.logoUrl = logoUrl.strip().lower()

    def get_parties(self):
        """method to get all parties"""
        con = init_db()
        cur = con.cursor()
        query = "SELECT party_id, name,hqAddress,logoUrl from Party;"
        cur.execute(query)
        data = cur.fetchall()
        party_list = []

        for i, items in enumerate(data):
            party_id, name, hqAddress, logoUrl = items
            party = dict(
                party_id=party_id,
                name=name,
                hqAddress=hqAddress,
                logoUrl=logoUrl
            )
            party_list.append(party)

        return dict(status=200, data=party_list)

    def get_party(self, party_id):
        con = init_db()
        cur = con.cursor()
        if not BaseModel().check_exists('party', 'party_id', party_id):
            return dict(status=404, data={"error": "No party with ID:{}".format(party_id)})
        query = "SELECT party_id, name,hqAddress,logoUrl from Party where party_id = {};".format(
            party_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        party_list = []
        party = dict(
            party_id=data[0],
            name=data[1],
            hqAddress=data[2],
            logoUrl=data[3]
        )
        party_list.append(party)

        return dict(status=200, data=party_list)

    def save_party(self):
        party = {
            "name": self.name,
            "hqAddress": self.hqAddress,
            "logoUrl": self.logoUrl
        }

        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO PARTY (name,hqAddress,logoUrl) VALUES \
             (%(name)s,%(hqAddress)s,%(logoUrl)s) Returning party_id;"""
        bm = BaseModel()
        if bm.check_exists('party', 'name', party['name'].strip().lower()):
            return dict(status=409, error="Cannot have more than one party with the same name")
        cur.execute(query, party)
        party_id = cur.fetchone()[0]
        con.commit()
        con.close()
        success = {
            "status": 201,
            "message": "Successfully created {} party with ID:{}".format(party['name'], party_id)

        }
        return success

    def edit_party(self, party_id):
        con = init_db()
        cur = con.cursor()
        uname = ""
        uhqAddress = ""
        ulogoUrl = ""
        if not BaseModel().check_exists('party', 'party_id', party_id):
            return dict(status=404, error="No party with ID:{}".format(party_id))

        query = "Update party set "

        if 'name' in request.json and request.json['name'].strip():
            uname = request.json['name'].strip().lower()
            if BaseModel().check_exists('party', 'name', uname):
                return dict(status=409, error="Cannot have more than one party with the same name")
            query += "name = '" + str(uname) + "'"
        if 'hqAddress' in request.json and request.json['hqAddress'].strip():
            uhqAddress = request.json['hqAddress'].strip().lower()
            if 'name' in request.json and request.json['name'].strip():
                query += ",hqAddress = '" + str(uhqAddress) + "'"
            else:
                query += "hqAddress = '" + str(uhqAddress) + "'"
        if 'logoUrl' in request.json and request.json['logoUrl'].strip():
            ulogoUrl = request.json['logoUrl'].strip().lower()
            if 'hqAddress' in request.json and request.json['hqAddress'].strip() or 'name' in request.json and request.json['name'].strip():
                query += ",logoUrl = '" + str(ulogoUrl) + "'"
            else:
                query += "logoUrl = '" + str(ulogoUrl) + "'"

        query += " where party_id = {}".format(party_id)
        # import pdb; pdb.set_trace()
        cur.execute(query)

        con.commit()
        con.close()

        return dict(self.get_party(party_id), message="Changes made successfully")

    def delete_party(self, party_id):
        con = init_db()
        cur = con.cursor()

        if not BaseModel().check_exists('party', 'party_id', party_id):
            return dict(status=404, error="No party with ID:{}".format(party_id))

        query = " delete from party where party_id = {}".format(party_id)
        # import pdb; pdb.set_trace()
        cur.execute(query)

        con.commit()
        con.close()

        return dict(status=200, message="Party successfully deleted")
