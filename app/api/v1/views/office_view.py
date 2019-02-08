from flask import Blueprint, request, jsonify
from app.api.v1.models.office_model import PoliticalOffice

bpoffice = Blueprint('office', __name__)


@bpoffice.route('/', methods=['POST'])
def create_office():
    """ Creating a political party"""
    office = PoliticalOffice()
    if request.json['name']:
        name = request.json['name']
        office.name = name
    if request.json['type']:
        office_type = request.json['type']
        office.office_type = office_type
      
    if name and office_type:
        return jsonify(office.create_office())
    else:
        return dict(status=400, data={"error": "Bad request. Enter all fields"})

    # POLITICAL_PARTIES.append(party)
    
    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpoffice.route('/', methods=['GET'])
def offices_all():
    """function to retrieve all political offices"""
    office = PoliticalOffice()
    return jsonify(office.get_offices())


@bpoffice.route('/<int:id>', methods=['GET'])
def offices_id(id):
    """function to retrieve a specific political office"""

    office = PoliticalOffice()

    return jsonify(office.get_office(id))
