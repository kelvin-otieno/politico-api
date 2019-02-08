"""file with helper methods for testing office and party classes"""
from flask import json


def create_party(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v1/parties/', data=json.dumps(data), content_type='application/json')


def create_office(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v1/offices/', data=json.dumps(data), content_type='application/json')
