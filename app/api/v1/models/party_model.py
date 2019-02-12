"""Political Party Model"""
from flask import request, Response


class PoliticalParty():
    """defining the model of a political party"""
    political_parties = []

    id = 0
    name = ""
    hqAddress = ""
    logoUrl = ""

    def __init__(self):
        self.political_parties = [
            {
                'id': 1,
                'name': 'ANC',
                'hqAddress': 'Bungoma',
                'logoUrl': 'amani.png'
            },
            {
                'id': 2,
                'name': 'NASA',
                'hqAddress': 'Nairobi',
                'logoUrl': 'nasa.png'
            },
            {
                'id': 3,
                'name': 'Jubilee',
                'hqAddress': 'Nairobi',
                'logoUrl': 'jubilee.png'
            },
            {
                'id': 4,
                'name': 'TIPTIP',
                'hqAddress': 'Makueni',
                'logoUrl': 'tip.png'
            }
        ]

    def create_party(self):
        """method to create a new party"""
        party = {
            'id': len(self.political_parties) + 1,
            'name': self.name,
            'hqAddress': self.hqAddress,
            'logoUrl': self.logoUrl
        }

        self.political_parties.append(party)
        return dict(status=201, data=self.political_parties)

    def edit_party(self, id):
        """method to edit a party"""
        exists = False
        # data = request.get_json()
        # name = data['name']
        #exists = True
        if self.political_parties:
            for party in self.political_parties:
                if party['id'] == id:
                    exists = True
                    if 'name' in request.json and request.json['name']:
                        party['name'] = request.json['name']
                    if 'hqAdress' in request.json and request.json['hqAddress']:
                        party['hqAddress'] = request.json['hqAddress']
                    if 'logoUrl' in request.json and request.json['logoUrl']:
                        party['logoUrl'] = request.json['logoUrl']
                    # return dict(status=Response.status_code, data=self.political_parties)

        if not exists:
            return dict(status=400, data={"error": "No party with ID:{}".format(id)})
        else:
            return dict(status=201, data=self.political_parties)

    def get_parties(self):
        """method to get all parties"""
        if self.political_parties:
            return dict(status=200, data=self.political_parties)
        else:
            return dict(status=404, data={"error": "Not Found any parties"})

    def get_party(self, id):
        """method to get an individual party"""
        exists = False
        if self.political_parties:
            for party in self.political_parties:
                if party['id'] == id:
                    exists = True
                    return dict(status=200, data=party)
        if not exists:
            return dict(status=400, data={"error": "Bad Request. No party with ID:{}".format(id)})

    def delete_party(self, id):
        """method to delete a party"""
        exists = False
        if self.political_parties:
            for party in self.political_parties:
                if party['id'] == id:
                    exists = True
                    self.political_parties.remove(party)

        if not exists:
            return dict(status=400, data={"error": "No party with ID:{}".format(id)})
        else:
            return dict(status=200, data=[{"message":"Successfully deleted party with ID:{}".format(id)}])
