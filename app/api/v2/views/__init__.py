from flask import request, jsonify
from functools import wraps
import jwt
import os

key = os.getenv('SECRET_KEY')


def token_auth(f):
    @wraps(f)
    def check_token(*args, **kwargs):
        if 'token' in request.headers:
            token = request.headers['token']
            if token.strip():
                try:
                    jwt.decode(token, key)
                except:
                    return jsonify(dict(status=400, error="Bad request. Invalid token")), 400
            else:
                return jsonify(dict(status=400, error="Bad request. Empty token string")), 400
        else:
            return jsonify(dict(status=400, error="Bad request. No token found")), 400
        return f(*args, **kwargs)
    return check_token