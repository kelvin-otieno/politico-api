"""This file is resposible for handling

the routes that call methods that

are responsible for handling the voting process"""


from flask import Blueprint, request, jsonify
from app.api.v2.models.vote_model import Vote

bpvote = Blueprint('vote', __name__)
vote = Vote()


@bpvote.route('votes/', methods=['POST'])
def cast_vote():
    """This route calls the method that handles the casting of votes"""
    if request.json['candidate_id'] and request.json['office_id'] and request.json['voter_id']:
        candidate_id = request.json['candidate_id']
        voter_id = request.json['voter_id']
        office_id = request.json['office_id']
        vote.candidate_id = candidate_id
        vote.voter_id = voter_id
        vote.office_id = office_id

        return jsonify(vote.cast_vote())

    else:
        return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))


@bpvote.route('office/<int:office_id>/result/', methods=['GET'])
def count_votes(office_id):
    """This route calls the method that handles the counting of votes"""
    return jsonify(vote.count_votes(office_id))
