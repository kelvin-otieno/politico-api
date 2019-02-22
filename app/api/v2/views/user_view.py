from flask import Blueprint, request, jsonify
from app.api.v2.models.user_model import User
import bcrypt
from . import token_auth
import re
from . import validation

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
    # import pdb
    # pdb.set_trace()
    if 'email' in request.json and 'password' in request.json and 'confirm_password' in request.json:
        if request.json['email'].strip() and request.json['password'].strip() and request.json['confirm_password'].strip():
            email = request.json['email']
            if not validation.isValidEmail(email):
                return jsonify(dict(status=400, error="")), 400
            password = request.json['password']
            confirm_password = request.json['confirm_password']
            if password != confirm_password:
                return jsonify(dict(status=400, error="Password and confirm password must be the same")), 400
            elif validation.isValidPassword(password):
                return jsonify(dict(status=400, error="Password length must be greater than 6 characters")), 400
            else:
                return jsonify(user.reset_password(email.strip(), password.strip()))

        else:
            return jsonify(dict(status=400, data={"error": "email cannot be empty"}))
    else:
        return jsonify(dict(status=400, error="Provide email"))


@bpuser.route('/', methods=['GET'])
def users_all():
    """function to retrieve all users"""
    return jsonify(user.get_users())
