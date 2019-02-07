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


@bpparty.route('/', methods=['POST'])
def create_party():
    """ Creating a political party"""
    code = request.json['code']
    full_name = request.json['full_name']
    logo = request.json['logo']
    slogan = request.json['slogan']

    party = PoliticalParty()
    party.code = code
    party.full_name = full_name
    party.logo = logo
    party.slogan = slogan

    party.create_party()
    # POLITICAL_PARTIES.append(party)
    return jsonify(party.get_parties())
    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpparty.route('/<int:id>', methods=['PUT'])
def edit_party(id):
    pparty = PoliticalParty()

    return jsonify(pparty.edit_party(id))


@bpparty.route('/<int:id>', methods=['DELETE'])
def delete_party(id):
    """ Deleting a political party"""
    party = PoliticalParty()

    return jsonify(party.delete_party(id))
