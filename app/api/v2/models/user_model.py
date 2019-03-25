from app.database_config import Database
from app.api.v2.models.basemodel import BaseModel
from flask import request
import jwt
import bcrypt
import datetime
import os
from flask_mail import Mail, Message
import app

# from run import mail
# from run import app

firstname = ""
lastname = ""
othername = ""
email = ""
phoneNumber = ""
passportUrl = ""
password = ""

db = None


class User(BaseModel):

    def __init__(self):
        self.db = Database()

    def register_user(self):
        # destroydb()
        user = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othername": self.othername,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "passportUrl": self.passportUrl,
            "password": self.password
        }

        con = self.db.init_db()
        # import pdb
        # pdb.set_trace()
        cur = con.cursor()
        def_query = "INSERT INTO USERS (firstname,lastname,othername,email,phoneNumber,passportUrl,isAdmin,password)  VALUES ('elsie', 'chesang','keter','admin@admin.com','0712561541','https://pic.png',true,'admin')"
        query = """INSERT INTO USERS (firstname,lastname,othername,email,phoneNumber,passportUrl,password) VALUES \
             (%(firstname)s,%(lastname)s,%(othername)s,%(email)s,%(phoneNumber)s,%(passportUrl)s,%(password)s) Returning user_id;"""
        # import pdb
        # pdb.set_trace()
        bm = BaseModel()
        if bm.check_exists('users', 'email', user['email'].strip().lower()):
            return dict(status=409, error="Cannot have more than one user with the same email")

        if not bm.check_exists('users', 'firstname', 'elsie'):
            try:
                cur.execute(def_query)
            except Exception as e:
                pass

        try:
            cur.execute(query, user)
        except Exception as e:
            return dict(status=409, error=str(e))

        user_id = cur.fetchone()[0]
        con.commit()
        con.close()
        # token = jwt.encode({
        #     'user': email,
        #     'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
        # }, 'secretkey')
        user_list = []
        user_dict = dict(
            id=user_id, name=user['firstname'], email=user['email'], phone=user['phoneNumber'])
        user_list.append(user_dict)
        token = jwt.encode({
            'user': email,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
        }, os.getenv('SECRET_KEY'))
        success = {
            "status": 201,
            "data": user_list,
            "token": token.decode('UTF-8'),
            "message": "Successfully created user {} with ID:{}".format(user['firstname'], user_id)
        }
        return success

    def login_user(self, email, password):
        """login user"""
        con = self.db.init_db()
        cur = con.cursor()
        if not BaseModel().check_exists('users', 'email', email):
            return dict(status=404, error="No user with email:{}".format(email))
        query = "SELECT firstname,lastname,phonenumber,isAdmin,password,user_id,passporturl from users where email = '" + email + "'"
        cur.execute(query)
        data = cur.fetchall()[0]

        if password != data[4]:
            return dict(status=401, error='Not authorised :wrong username/password')
        else:
            isAdmin = bool(data[3])
            user_id = int(data[5])
            token = jwt.encode({
                'user_id': user_id,
                'user': email,
                'role': isAdmin,
                'exp': datetime.datetime.utcnow()+datetime.timedelta(hours=5)
            }, os.getenv('SECRET_KEY'))
            user = dict(
                firstname=data[0],
                lastname=data[1],
                phoneNumber=data[2],
                isAdmin=data[3],
                user_id=data[5],
                passportUrl=data[6]

            )
        con.commit()
        con.close()
        return dict(status=200, data={"user": user, "token": token.decode('UTF-8')})

    def get_users(self):
        """method to get all users"""
        con = self.db.init_db()
        cur = con.cursor()
        query = "SELECT user_id,firstname, email,phoneNumber,isAdmin from users;"
        cur.execute(query)
        data = cur.fetchall()
        user_list = []

        for i, items in enumerate(data):
            user_id, firstname, email, phoneNumber, isAdmin = items
            user = dict(
                user_id=user_id,
                firstname=firstname,
                email=email,
                phoneNumber=phoneNumber,
                isAdmin=isAdmin
            )
            user_list.append(user)

        return dict(status=200, data=user_list)

    def get_user(self, user_id):
        """method to get all users"""
        con = self.db.init_db()
        cur = con.cursor()
        query = "SELECT user_id,firstname,lastname,othername,email,phoneNumber,passportUrl,password from users where user_id = {};".format(
            user_id)
        cur.execute(query)
        data = cur.fetchall()
        user_list = []

        for i, items in enumerate(data):
            user_id, firstname, lastname, othername, email, phoneNumber, passportUrl, password = items
            user = dict(
                user_id=user_id,
                firstname=firstname,
                lastname=lastname,
                othername=othername,
                email=email,
                phoneNumber=phoneNumber,
                passportUrl=passportUrl,
                password=password
            )
            user_list.append(user)

        return dict(status=200, data=user_list)

    def send_link(self, email):
        """reset password"""
        if not BaseModel().check_exists('users', 'email', email):
            return dict(status=404, error="No user with email:{}".format(email))
        user_id = BaseModel.getFieldVal(
            self, "users", "user_id", "email", email)
        token = jwt.encode({
            'user_id': user_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},
            os.getenv('SECRET_KEY'))

        link = "127.0.0.1:5500/UI/reset_password.html?" + \
            str(token.decode('UTF-8'))
        # self.configure_email()

        msg = Message('Password Reset for Politico',
                      sender='kelvinotieno06@gmail.com', recipients=[email])
        msg.body = "Click on the link below to reset password \n "
        msg.body += link
        app.mail.send(msg)
        return dict(status=200, data={"message": "password reset link sent"})

    def reset_password(self, user_id, password):
        """reset password"""
        con = self.db.init_db()
        cur = con.cursor()
        query = "UPDATE users set password = '{}' where user_id = '{}'".format(
            password, user_id)
        try:
            cur.execute(query)
            con.commit()
            con.close()
        except Exception as e:
            return dict(status=500, error=str(e))

        return dict(status=200, data={"message": "password set successfully", "email": str(email)})

    def update_user(self, user_id):
        con = self.db.init_db()
        cur = con.cursor()
        uname = ""
        uhqAddress = ""
        ulogoUrl = ""
        if not BaseModel().check_exists('users', 'user_id', user_id):
            return dict(status=404, error="No user with ID:{}".format(user_id))

        query = "Update users set "
        if 'email' in request.json and request.json['email'].strip():
            email = request.json['email'].strip().lower()
            if BaseModel().check_exists('users', 'email', email):
                if email != BaseModel.getFieldVal(self, 'users', 'email', 'user_id', user_id):
                    return dict(status=409, error="Cannot have more than one user with the same email")
            query += "email = '" + str(email) + "'"
        if 'phoneNumber' in request.json and request.json['phoneNumber'].strip():
            phoneNumber = request.json['phoneNumber'].strip().lower()
            if BaseModel().check_exists('users', 'phoneNumber', phoneNumber):
                if phoneNumber != BaseModel.getFieldVal(self, 'users', 'phoneNumber', 'user_id', user_id):
                    return dict(status=409, error="Cannot have more than one user with the same phoneNumber")
            query += ",phoneNumber = '" + str(phoneNumber) + "'"
        if 'firstname' in request.json and request.json['firstname'].strip():
            firstname = request.json['firstname'].strip().lower()
            query += ",firstname = '" + str(firstname) + "'"
        if 'lastname' in request.json and request.json['lastname'].strip():
            lastname = request.json['lastname'].strip().lower()
            query += ",lastname = '" + str(lastname) + "'"
        if 'othername' in request.json and request.json['othername'].strip():
            othername = request.json['othername'].strip().lower()
            query += ",othername = '" + str(othername) + "'"
        if 'passportUrl' in request.json and request.json['passportUrl'].strip():
            passportUrl = request.json['passportUrl'].strip().lower()
            query += ",passportUrl = '" + str(passportUrl) + "'"
        if 'password' in request.json and request.json['password'].strip():
            password = request.json['password'].strip().lower()
            query += ",password = '" + str(password) + "'"

        query += " where user_id = {}".format(user_id)

        cur.execute(query)

        con.commit()
        con.close()

        return dict(self.get_user(user_id), message="Changes made successfully")
