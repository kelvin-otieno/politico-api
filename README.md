[![Build Status](https://travis-ci.org/kelvin-otieno/politico-api.svg?branch=develop)](https://travis-ci.org/kelvin-otieno/politico-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/e90d88ca20de549f2961/maintainability)](https://codeclimate.com/github/kelvin-otieno/politico-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/kelvin-otieno/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/kelvin-otieno/politico-api?branch=develop)

# Politico API

This app provides the API for the politico project. It allows admin users to:

- create a political party
- delete a political party
- edit a political party
- retrieve all parties created
- retrieve a single party
- create a political office
- retrieve all political offices
- retrieve a single political office

# Hosting Link
```
https://vast-mountain-54945.herokuapp.com/api/v1/parties/
https://vast-mountain-54945.herokuapp.com/api/v1/offices/
```

# Installation

Clone the application from the link `https://github.com/kelvin-otieno/politico-api.git` or simply download the zipped file and extract to your computer.

# Run

Navigate to the root of the project then from the terminal execute `python run.py`

# Testing

To test, while on the root folder, run `pytest -v tests/` or simply navigate to the tests folder and run `pytest -v`

# Endpoints

| Endpoint             |      Functionality      | Method |
| -------------------- | :---------------------: | ------ |
| /api/v1/parties/     |     Create a party      | POST   |
| /api/v1/parties/     |     Get all parties     | GET    |
| /api/v1/parties/<id> |  Get a specific party   | GET    |
| /api/v1/parties/<id> |  Edit a specific party  | PUT    |
| /api/v1/parties/<id> | Delete a specific party | DELETE |
| /api/v1/offices/     |    Create an office     | POST   |
| /api/v1/offices/<id> |  Get a specific office  | GET    |
| /api/v1/offices/     |     Get all offices     | GET    |

## PAYLOADS

# Creating a party

`/api/v1/parties/`

Payload  
```
{ 'name': 'ANC',        
    'hqAddress': 'Bungoma',       
    'logoUrl': 'amani.png'       
    }
```


Response  
```
{
    "data": [
        {
            "hqAddress": "Bungoma",
            "id": 1,
            "logoUrl": "amani.png",
            "name": "ANC"
        }
    ],
    "status": 201
}
    
```


# Editing a party

`/api/v1/parties/1`

The example below shows editing the hqAddress of party with id 1 from Bungoma to Busia

Payload    
```
{ 'hqAddress': 'Busia'}
```


Response  
```
{
    "data": [
        {
            "hqAddress": "Busia",
            "id": 1,
            "logoUrl": "amani.png",
            "name": "ANC"
        }
    ],
    "status": 201
}
    
```

# Licence

© Kelvin Otieno
