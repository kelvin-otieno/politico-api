from app.database_config import Database

db = None


class BaseModel(object):

    def __init__(self):
        self.db = Database()

    def check_exists(self, table_name, field_name, value):
        con = self.db.init_db()
        cur = con.cursor()
        query = "SELECT * FROM {} WHERE {}.{}='{}'".format(
            table_name, table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchall()
        if resp:
            return True
        else:
            return

    def getFieldVal(self, table_name, field_name, pk, value):
        con = self.db.init_db()
        cur = con.cursor()
        query = "SELECT {} FROM {} WHERE {}='{}'".format(
            field_name, table_name, pk, value)
        cur.execute(query)
        resp = cur.fetchall()
        name = resp[0][0]
        return name

    def returnResult(self, query):
        con = self.db.init_db()
        cur = con.cursor()
        query = query
        cur.execute(query)
        resp = cur.fetchall()
        result = resp[0][0]
        return result
