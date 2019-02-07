from flask import Blueprint, request, jsonify
from app.api.v1.models.party_model import PoliticalParty

bpparty = Blueprint('party', __name__)


@bpparty.route('/', methods=['GET'])
def parties_all():
    """function to retrieve all political parties"""
    party = PoliticalParty()
    return jsonify(party.get_parties())
