from flask import Blueprint, request, jsonify
from app.api.v1.models.party_model import PoliticalParty

bpparty = Blueprint('party', __name__)


@bpparty.route('/', methods=['GET'])
def parties_all():
    """function to retrieve all political parties"""
    party = PoliticalParty()
    return jsonify(party.get_parties())


@bpparty.route('/<int:id>', methods=['GET'])
def parties_id(id):
    """function to retrieve a specific political party"""

    parties = PoliticalParty()

    return jsonify(parties.get_party(id))
