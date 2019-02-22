from flask import Blueprint, request, jsonify
from app.api.v2.models.party_model import PoliticalParty
from . import token_auth, is_admin, validation

bppartyv2 = Blueprint('partyv2', __name__)
party = PoliticalParty()


@bppartyv2.route('/', methods=['GET'])
@token_auth
def parties_all():
    """function to retrieve all political parties"""

    return jsonify(party.get_parties())


@bppartyv2.route('/<int:id>', methods=['GET'])
@token_auth
def parties_id(id):
    """function to retrieve a specific political party"""

    # parties = PoliticalParty()

    return jsonify(party.get_party(id))


@bppartyv2.route('/', methods=['POST'])
@token_auth
def create_party():
    """ Creating a political party"""
    if not is_admin():
        return jsonify(dict(status=401, data={"Not authorized": "Only admins can create a party"}))
    if request.json['name'].strip() and request.json['hqAddress'].strip() and request.json['logoUrl'].strip():
        name = request.json['name']
        if not validation.isValidName([name]):
            return jsonify(status=400, error="A valid name contains only alphabets"), 400
        hqAddress = request.json['hqAddress']
        logoUrl = request.json['logoUrl']
        # party = PoliticalParty()
        party.name = name.strip().lower()
        party.hqAddress = hqAddress.strip().lower()
        party.logoUrl = logoUrl.strip().lower()
        # import pdb; pdb.set_trace()
        # POLITICAL_PARTIES.append(party)
        return jsonify(party.save_party())

    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))

    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg
# import pdb; pdb.set_trace()


@bppartyv2.route('/<int:id>', methods=['PATCH'])
@token_auth
def edit_party(id):
    # pparty = PoliticalParty()
    if not is_admin():
        return jsonify(dict(status=401, data={"Not authorized": "Only admins can edit a party"}))
    if 'name' in request.json and not request.json['name'].strip():
        return jsonify(dict(status=400, error="Bad request. You cannot have a blank field"))
    if 'hqAddress' in request.json and not request.json['hqAddress'].strip():
        return jsonify(dict(status=400, error="Bad request. You cannot have a blank field"))
    if 'logoUrl' in request.json and not request.json['logoUrl'].strip():
        return jsonify(dict(status=400, error="Bad request. You cannot have a blank field"))

    return jsonify(party.edit_party(id))


@bppartyv2.route('/<int:id>', methods=['DELETE'])
@token_auth
def delete_party(id):
    """ Deleting a political party"""
    # party = PoliticalParty()
    if not is_admin():
        return jsonify(dict(status=401, data={"Not authorized": "Only admins can delete a party"}))
    return jsonify(party.delete_party(id))
