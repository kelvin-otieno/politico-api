from flask import Blueprint, request, jsonify
from app.api.v2.models.user_model import User
import bcrypt
from . import token_auth
import re
from . import validation
import jwt
import os

bpuser = Blueprint('user', __name__)
user = User()


@bpuser.route('/signup', methods=['POST'])
def create_user():
    """ Creating a user"""

    if request.json['firstname'].strip() and request.json['othername'].strip() and request.json['lastname'].strip() and request.json['email'].strip() and request.json['phoneNumber'].strip() and request.json['passportUrl'].strip() and request.json['password'].strip():

        if len(request.json['password'].strip()) < 6:
            return jsonify(dict(status=400, error='password must have a minimum length of 6'))
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        othername = request.json['othername']
        email = request.json['email']
        phoneNumber = request.json['phoneNumber']
        passportUrl = request.json['passportUrl']
        password = request.json['password']
        if not validation.isValidName([firstname, lastname, othername]):
            return jsonify(status=400, error="A valid name contains only alphabets"), 400
        if not validation.isValidEmail(email):
            return jsonify(status=400, error="Invalid email address")
        if not validation.isValidPhoneNumber(phoneNumber):
            return jsonify(status=400, error="Invalid phone number")
        if not validation.isValidPassword(password):
            return jsonify(status=400, error="Invalid password")
        if not validation.isValidPassport(passportUrl):
            return jsonify(status=400, error="Invalid passport")

        user.firstname = firstname.strip().lower()
        user.lastname = lastname.strip().lower()
        user.othername = othername.strip().lower()
        user.email = email.strip().lower()
        user.phoneNumber = phoneNumber.strip().lower()
        user.passportUrl = passportUrl.strip().lower()
        user.othername = othername.strip().lower()
        user.password = password

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


@bpuser.route('/reset', methods=['POST'])
def reset_pwd():
    """ reset user password"""
    if 'password' in request.json and 'token' in request.json:
        if request.json['password'].strip():
            password = request.json['password']
            if not validation.isValidPassword(password):
                return jsonify(dict(status=400, error="Password length must be greater than 6 characters")), 400
            else:
                try:
                    data = jwt.decode(
                        request.json['token'], os.getenv('SECRET_KEY'))
                    user_id = data['user_id']

                except Exception as e:
                    return jsonify(dict(status=400, error="invalid token"))
                return jsonify(user.reset_password(user_id, password))
        else:
            return jsonify(dict(status=400, error="Provide password"))


@bpuser.route('/', methods=['GET'])
def users_all():
    """function to retrieve all users"""
    return jsonify(user.get_users())


@bpuser.route('/<int:id>', methods=['GET'])
def get_user(id):
    """function to retrieve specific user"""
    return jsonify(user.get_user(id))


@bpuser.route('/<int:id>', methods=['PUT'])
def update_user(id):
    """function to update user"""
    return jsonify(user.update_user(id))


@bpuser.route('/send_link', methods=['POST'])
def send_link():
    """function to send password reset link"""
    if 'email' in request.json:
        email = request.json['email']
        return jsonify(user.send_link(email))
    else:
        return jsonify(status=400, error="Bad request.Enter email")
