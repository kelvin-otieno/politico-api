import pdb
from flask import request, jsonify
from functools import wraps
import jwt
import os


key = os.getenv('SECRET_KEY')

isadmin = False


def token_auth(f):
    @wraps(f)
    def check_token(*args, **kwargs):
        if 'token' in request.headers:
            token = request.headers['token']
            if token.strip():
                try:
                    data = jwt.decode(token, key)
                    role = data['role']
                    isadmin = bool(role)
                except:
                    return jsonify(dict(status=400, error="Bad request. Invalid token")), 400
            else:
                return jsonify(dict(status=400, error="Bad request. Empty token string")), 400
        else:
            return jsonify(dict(status=401, error="Not authorised")), 401
        return f(*args, **kwargs)
    return check_token


def is_admin():
    token = request.headers['token']
    data = jwt.decode(token, key)
    role = data['role']
    isadmin = bool(role)
    return isadmin


def loggedID():
    token = request.headers['token']
    data = jwt.decode(token, key)
    user_id = int(data['user_id'])
    return user_id
