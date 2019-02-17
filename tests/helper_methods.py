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


def create_office_v2(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v2/offices/', data=json.dumps(data), content_type='application/json')


def create_party_v2(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v2/parties/', data=json.dumps(data), content_type='application/json')


def create_user(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v2/auth/signup/', data=json.dumps(data), content_type='application/json')

def create_candidate(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v2/office/1/register/', data=json.dumps(data), content_type='application/json')

def create_vote(self, data):
    """endpoint to create new party"""
    return self.client.post(
        path='/api/v2/votes/', data=json.dumps(data), content_type='application/json')
