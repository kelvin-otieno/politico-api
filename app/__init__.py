"""Class to initialise our app"""
from flask import Flask
from app.api.v1.views.party_view import bpparty
from app.api.v1.views.office_view import bpoffice
from app.api.v2.views.party_view import bppartyv2
from app.api.v2.views.office_view import bpofficev2
from app.api.v2.views.user_view import bpuser
from app.api.v2.views.candidate_view import bpcandidate
from app.api.v2.views.vote_view import bpvote
from app.api.v2.views.petition_view import bppetition
from . import database_config


def create_app():
    """Method to create our app"""
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'secretkey'
    # database_config.destroydb()
    app.url_map.strict_slashes = False
    app.register_blueprint(bpparty, url_prefix='/api/v1/parties')
    app.register_blueprint(bpoffice, url_prefix='/api/v1/offices')
    app.register_blueprint(bppartyv2, url_prefix='/api/v2/parties')
    app.register_blueprint(bpofficev2, url_prefix='/api/v2/offices')
    app.register_blueprint(bpuser, url_prefix='/api/v2/auth')
    app.register_blueprint(bpcandidate, url_prefix='/api/v2/office')
    app.register_blueprint(bpvote, url_prefix='/api/v2/')
    app.register_blueprint(bppetition, url_prefix='/api/v2/petitions')
    return app
