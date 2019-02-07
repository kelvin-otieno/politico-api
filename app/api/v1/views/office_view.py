from flask import Blueprint, request, jsonify
from app.api.v1.models.office_model import PoliticalOffice

bpoffice = Blueprint('office', __name__)


@bpoffice.route('/', methods=['POST'])
def create_office():
    """ Creating a political party"""
    name = request.json['name']
    level = request.json['level']

    office = PoliticalOffice()
    office.name = name
    office.level = level

    # POLITICAL_PARTIES.append(party)
    return jsonify(office.create_office())
    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg


@bpoffice.route('/', methods=['GET'])
def offices_all():
    """function to retrieve all political offices"""
    office = PoliticalOffice()
    return jsonify(office.get_offices())
