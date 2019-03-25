# from flask import Blueprint, request, jsonify
# from app.api.v2.models.petition_model import Petition
# from . import token_auth, is_admin, validation, loggedID

# bppetition = Blueprint('petition', __name__)
# petition = Petition()


# @bppetition.route('/', methods=['POST'])
# @token_auth
# def create_petition():
#     """ Creating a petition"""
#     if 'office_id' not in request.json or 'text' not in request.json or 'evidence' not in request.json:
#         return jsonify(dict(status=400, data={"error": "Bad request. Kindly check if you have the fields: office, text and evidence"}))
#         # import pdb
#         # pdb.set_trace()
#     if not request.json['office_id'] or not request.json['text'].strip() or not request.json['evidence'].strip():
#         return jsonify(dict(status=400, data={"error": "Bad request. Kindly check if you have the fields: office_id, text and evidence"}))

#     if request.json['office_id']:
#         office_id = request.json['office_id']
#         petition.office_id = office_id
#     if request.json['text'].strip():
#         text = request.json['text']
#         petition.text = text
#     if request.json['evidence'].strip():
#         evidence = request.json['evidence']
#         petition.evidence = evidence

#     petition.user_id = loggedID()
#     if office_id and text and evidence:
#         return jsonify(petition.save_petition())
#     else:
#         return jsonify(dict(status=400, data={"error": "Bad request. Enter all fields"}))


# @bppetition.route('/', methods=['GET'])
# @token_auth
# def petitions_all():
#     """function to retrieve all petitions"""
#     return jsonify(petition.get_petitions())
