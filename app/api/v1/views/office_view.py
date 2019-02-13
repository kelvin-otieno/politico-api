from flask import Blueprint, request, jsonify
from app.api.v1.models.office_model import PoliticalOffice

bpoffice = Blueprint('office', __name__)
office = PoliticalOffice()


@bpoffice.route('/', methods=['POST'])
def create_office():
    """ Creating a political party"""

    if 'name' not in request.json or 'type' not in request.json:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))
        # import pdb
        # pdb.set_trace()
    if not request.json['name'].strip() or not request.json['type'].strip():
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))

    if request.json['name'].strip():
        # import pdb
        # pdb.set_trace()
        name = request.json['name']
        office.name = name
    if request.json['type'].strip():
        # import pdb; pdb.set_trace()
        office_type = request.json['type']
        if office_type.strip().lower() != 'federal' and office_type.strip().lower() != 'legislative' and office_type.strip().lower() != 'state' and office_type.strip().lower() != 'local government':
            #  import pdb; pdb.set_trace()
            return jsonify(dict(status=400, data={"Bad request": "Office can only be legislative, state, federal or local government"}))
        else:
            office.office_type = office_type.strip()

    if name and office_type:
        return jsonify(office.create_office())
    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))

    # POLITICAL_PARTIES.append(party)

    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpoffice.route('/', methods=['GET'])
def offices_all():
    """function to retrieve all political offices"""
    # office = PoliticalOffice()
    return jsonify(office.get_offices())


@bpoffice.route('/<int:id>', methods=['GET'])
def offices_id(id):
    """function to retrieve a specific political office"""

    # office = PoliticalOffice()

    return jsonify(office.get_office(id))
