"""Class to initialise our app"""
from flask import Flask
from app.api.v1.views.party_view import bpparty
from app.api.v1.views.office_view import bpoffice


def create_app():
    """Method to create our app"""
    app = Flask(__name__)
    app.register_blueprint(bpparty, url_prefix='/api/v1/parties')
    app.register_blueprint(bpoffice, url_prefix='/api/v1/offices')
    return app
