from flask import Blueprint, request, jsonify
from app.api.v2.models.candidate_model import Candidate

bpcandidate = Blueprint('candidate', __name__)
candidate = Candidate()


@bpcandidate.route('/<int:officeid>/register', methods=['POST'])
def create_candidate(officeid):
    """ Creating a candidate"""
    office_id = officeid
    if 'user_id' not in request.json:
        return jsonify(dict(status=400, data={"error": "Enter  user id"}))
        # import pdb
        # pdb.set_trace()
    if not request.json['user_id'] or not isinstance(request.json['user_id'], int):
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields. Value must be an integer"}))

    if request.json['user_id']:
        # import pdb
        # pdb.set_trace()
        user_id = request.json['user_id']
        candidate.user_id = user_id
        candidate.office_id = office_id
    # if request.json['office_id']:
    #     # import pdb; pdb.set_trace()
    #     office_id = request.json['office_id']

    #     candidate.office_id = office_id

    if user_id and office_id:
        return jsonify(candidate.save_candidate())
    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter required field"}))

    # POLITICAL_PARTIES.append(party)

    # return make_response(jsonify({"status": "OK", "message": "I am {}".format(full_name)}))
    # msg = "the name is " + full_name
    # return msg
