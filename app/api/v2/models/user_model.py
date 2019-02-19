from app.database_config import init_db
from app.api.v2.models.basemodel import BaseModel
from flask import request
import jwt
import bcrypt
import datetime
import os
# from run import app

firstname = ""
lastname = ""
othername = ""
email = ""
phoneNumber = ""
passportUrl = ""
isAdmin = False
password = ""


class User(BaseModel):
    def __init__(self):
        pass
        # self.name = name.strip().lower()
        # self.hqAddress = hqAddress.strip().lower()
        # self.logoUrl = logoUrl.strip().lower()

    def register_user(self):
        user = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othername": self.othername,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "passportUrl": self.passportUrl,
            "isAdmin": self.isAdmin,
            "password": self.password
        }

        con = init_db()
        # import pdb
        # pdb.set_trace()
        cur = con.cursor()
        query = """INSERT INTO USERS (firstname,lastname,othername,email,phoneNumber,passportUrl,isAdmin,password) VALUES \
             (%(firstname)s,%(lastname)s,%(othername)s,%(email)s,%(phoneNumber)s,%(passportUrl)s,%(isAdmin)s,%(password)s) Returning user_id;"""
        # import pdb
        # pdb.set_trace()
        bm = BaseModel()
        if bm.check_exists('users', 'email', user['email'].strip().lower()):
            return dict(status=409, error="Cannot have more than one user with the same email")
        cur.execute(query, user)
        user_id = cur.fetchone()[0]
        con.commit()
        con.close()
        # token = jwt.encode({
        #     'user': email,
        #     'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
        # }, 'secretkey')
        success = {
            "status": 201,
            "message": "Successfully created user {} with ID:{}".format(user['firstname'], user_id)
        }
        return success

    def login_user(self, email, password):
        """login user"""
        con = init_db()
        cur = con.cursor()
        if not BaseModel().check_exists('users', 'email', email):
            return dict(status=404, error="No user with email:{}".format(email))
        query = "SELECT firstname,lastname,phonenumber,isAdmin,password from users where email = '" + email + "'"
        cur.execute(query)
        data = cur.fetchall()[0]

        if password != data[4]:
            return dict(status=403, error='forbidden:wrong username/password')
        else:
            token = jwt.encode({
                'user': email,
                'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
            }, os.getenv('SECRET_KEY'))
            user = dict(
                firstname=data[0],
                lastname=data[1],
                phoneNumber=data[2],
                isAdmin=data[3]
            )
        return dict(status=200, data={"user": user, "token": token.decode('UTF-8')})
