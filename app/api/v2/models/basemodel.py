from app.database_config import init_db


class BaseModel(object):
    def __init__(self):
        pass

    def check_exists(self, table_name, field_name, value):
        con = init_db()
        cur = con.cursor()
        query = "SELECT * FROM {} WHERE {}.{}='{}'".format(
            table_name, table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchall()
        if resp:
            return True
        else:
            return False
