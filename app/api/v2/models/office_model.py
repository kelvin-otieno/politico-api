from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request

name = ""
office_type = ""


class PoliticalOffice(BaseModel):
    def __init__(self):
        pass
        self.name = name.strip().lower()
        self.office_type = office_type.strip().lower()

    def get_offices(self):
        """method to get all parties"""
        con = init_db()
        cur = con.cursor()
        query = "SELECT office_id, name,office_type from Office;"
        cur.execute(query)
        data = cur.fetchall()
        office_list = []

        for i, items in enumerate(data):
            office_id, name, office_type = items
            office = dict(
                office_id=office_id,
                name=name,
                office_type=office_type
            )
            office_list.append(office)

        return dict(status=200, data=office_list)

    def get_office(self, office_id):
        con = init_db()
        cur = con.cursor()
        if not BaseModel().check_exists('office', 'office_id', office_id):
            return dict(status=404, data={"error": "No office with ID:{}".format(office_id)})
        query = "SELECT office_id, name,office_type from Office where office_id = {};".format(
            office_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        office_list = []
        office = dict(
            office_id=data[0],
            name=data[1],
            office_type=data[2]

        )
        office_list.append(office)

        return dict(status=200, data=office_list)

    def save_office(self):
        office = {
            "name": self.name,
            "office_type": self.office_type
        }
        # import pdb
        # pdb.set_trace()
        con = init_db()
        cur = con.cursor()
        query = """INSERT INTO OFFICE (name,office_type) VALUES \
             (%(name)s,%(office_type)s) Returning office_id;"""
        bm = BaseModel()
        if bm.check_exists('office', 'name', office['name'].strip().lower()):
            return dict(status=409, error="Cannot have more than one office with the same name")
        # import pdb
        # pdb.set_trace()
        cur.execute(query, office)
        office_id = cur.fetchone()[0]
        con.commit()
        con.close()
        success = {
            "status": 201,
            "message": "Successfully created {} office with ID:{}".format(office['name'], office_id)

        }
        return success

    def edit_office(self, office_id):
        con = init_db()
        cur = con.cursor()
        uname = ""
        utype = ""

        if not BaseModel().check_exists('office', 'office_id', office_id):
            return dict(status=404, error="No office with ID:{}".format(office_id))

        query = "Update office set "

        if 'name' in request.json and request.json['name'].strip():
            uname = request.json['name'].strip().lower()
            if BaseModel().check_exists('office', 'name', uname):
                return dict(status=409, error="Cannot have more than one office with the same name")
            query += "name = '" + str(uname) + "'"
        if 'office_type' in request.json and request.json['office_type'].strip():
            utype = request.json['office_type'].strip().lower()
            if 'name' in request.json and request.json['name'].strip():
                query += ",office_type = '" + str(office_type) + "'"
            else:
                query += "office_type = '" + str(office_type) + "'"

            

        query += " where office_id = {}".format(office_id)
        # import pdb; pdb.set_trace()
        cur.execute(query)

        con.commit()
        con.close()

        return dict(self.get_office(office_id), message="Changes made successfully")

    def delete_office(self, office_id):
        con = init_db()
        cur = con.cursor()

        if not BaseModel().check_exists('office', 'office_id', office_id):
            return dict(status=404, error="No office with ID:{}".format(office_id))

        query = " delete from office where office_id = {}".format(office_id)
        # import pdb; pdb.set_trace()
        cur.execute(query)

        con.commit()
        con.close()

        return dict(status=200, message="Office successfully deleted")
