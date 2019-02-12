from flask import Blueprint, request, jsonify
from app.api.v1.models.party_model import PoliticalParty

bpparty = Blueprint('party', __name__)
party = PoliticalParty()

@bpparty.route('/', methods=['GET'])
def parties_all():
    """function to retrieve all political parties"""
    
   
    return jsonify(party.get_parties())


@bpparty.route('/<int:id>', methods=['GET'])
def parties_id(id):
    """function to retrieve a specific political party"""

    # parties = PoliticalParty()

    return jsonify(party.get_party(id))


@bpparty.route('/', methods=['POST'])
def create_party():
    """ Creating a political party"""
    if request.json['name'] and request.json['hqAddress'] and request.json['logoUrl']:
        name = request.json['name']
        hqAddress = request.json['hqAddress']
        logoUrl = request.json['logoUrl']
        # party = PoliticalParty()
        party.name = name
        party.hqAddress = hqAddress
        party.logoUrl = logoUrl

        
        # POLITICAL_PARTIES.append(party)
        return jsonify(party.create_party())
    else:
        return dict(status=400, data={"error": "Bad request. Enter all fields"})

    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpparty.route('/<int:id>', methods=['PUT'])
def edit_party(id):
    # pparty = PoliticalParty()

    return jsonify(party.edit_party(id))


@bpparty.route('/<int:id>', methods=['DELETE'])
def delete_party(id):
    """ Deleting a political party"""
    # party = PoliticalParty()

    return jsonify(party.delete_party(id))
