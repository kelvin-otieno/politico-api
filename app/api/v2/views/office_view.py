from flask import Blueprint, request, jsonify
from app.api.v2.models.office_model import PoliticalOffice
from . import token_auth, is_admin()

bpofficev2 = Blueprint('officev2', __name__)
office = PoliticalOffice()


@bpofficev2.route('/', methods=['POST'])
@token_auth
def create_office():
    """ Creating a political office"""
    if not is_admin():
        return jsonify(dict(status=401, data={"Not authorized": "Only admins can create an office"}))
    if 'name' not in request.json or 'office_type' not in request.json:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))
        # import pdb
        # pdb.set_trace()
    if not request.json['name'].strip() or not request.json['office_type'].strip():
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))

    if request.json['name'].strip():
        # import pdb
        # pdb.set_trace()
        name = request.json['name']
        office.name = name.strip().lower()
    if request.json['office_type'].strip():
        # import pdb; pdb.set_trace()
        office_type = request.json['office_type']
        if office_type.strip().lower() != 'federal' and office_type.strip().lower() != 'legislative' and office_type.strip().lower() != 'state' and office_type.strip().lower() != 'local government':
            #  import pdb; pdb.set_trace()
            return jsonify(dict(status=400, data={"Bad request": "Office can only be legislative, state, federal or local government"}))
        else:
            office.office_type = office_type.strip().lower()

    if name and office_type:
        return jsonify(office.save_office())
    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))

    # POLITICAL_PARTIES.append(party)

    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpofficev2.route('/', methods=['GET'])
@token_auth
def offices_all():
    """function to retrieve all political offices"""
    # office = PoliticalOffice()
    return jsonify(office.get_offices())


@bpofficev2.route('/<int:id>', methods=['GET'])
@token_auth
def offices_id(id):
    """function to retrieve a specific political office"""

    return jsonify(office.get_office(id))


@bpofficev2.route('/<int:id>', methods=['PUT'])
@token_auth
def edit_office(id):
    if not is_admin():
        return jsonify(dict(status=401, data={"Not authorized": "Only admins can create a candidate"}))
    if 'name' in request.json and not request.json['name'].strip():
        return jsonify(dict(status=400, error="Bad request. You cannot have a blank field"))
    if 'office_type' in request.json and not request.json['office_type'].strip():
        return jsonify(dict(status=400, error="Bad request. You cannot have a blank field"))

    return jsonify(office.edit_office(id))


@bpofficev2.route('/<int:id>', methods=['DELETE'])
@token_auth
def delete_office(id):
    """ Deleting a political office"""
    if not is_admin():
        return jsonify(dict(status=401, data="Not authorized. Only admins can delete an office"))
    return jsonify(office.delete_office(id))
