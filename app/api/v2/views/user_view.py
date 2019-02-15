from flask import Blueprint, request, jsonify
from app.api.v2.models.user_model import User
import bcrypt

bpuser = Blueprint('user', __name__)
user = User()


@bpuser.route('/signup', methods=['POST'])
def create_user():
    """ Creating a user"""

    if request.json['firstname'].strip() and request.json['othername'].strip() and request.json['lastname'].strip() and request.json['email'].strip() and request.json['phoneNumber'].strip() and request.json['passportUrl'].strip() and request.json['isAdmin'].strip() and request.json['password'].strip():

        if len(request.json['password'].strip()) < 6:
            return jsonify(dict(status=400, error='password must have a minimum length of 6'))
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        othername = request.json['othername']
        email = request.json['email']
        phoneNumber = request.json['phoneNumber']
        passportUrl = request.json['passportUrl']

        isAdmin = request.json['isAdmin']
        password = request.json['password']
        # party = PoliticalParty()
        # text = "here"
        # import pdb
        # pdb.set_trace()
        user.firstname = firstname.strip().lower()
        user.lastname = lastname.strip().lower()
        user.othername = othername.strip().lower()
        user.email = email.strip().lower()
        user.phoneNumber = phoneNumber.strip().lower()
        user.passportUrl = passportUrl.strip().lower()
        user.othername = othername.strip().lower()
        user.isAdmin = bool(isAdmin)
        user.password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        # import pdb; pdb.set_trace()
        # POLITICAL_PARTIES.append(party)
        return jsonify(user.register_user())

    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))


@bpuser.route('/login', methods=['POST'])
def login_user():
    """ login a user"""
    # import pdb
    # pdb.set_trace()
    if 'email' in request.json and 'password' in request.json:
        if request.json['email'].strip() and request.json['password'].strip():
            email = request.json['email']
            password = request.json['password']
            return jsonify(user.login_user(email.strip(), password.strip()))
        else:
            return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))
    else:
        return jsonify(dict(status=400, error="Provide email and password"))
