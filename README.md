[![Build Status](https://travis-ci.org/kelvin-otieno/politico-api.svg?branch=develop)](https://travis-ci.org/kelvin-otieno/politico-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/e90d88ca20de549f2961/maintainability)](https://codeclimate.com/github/kelvin-otieno/politico-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/kelvin-otieno/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/kelvin-otieno/politico-api?branch=develop)

# Politico API

Politico is a platform which both the politicians and citizens can use. It enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency

# Hosting Link

```
https://vast-mountain-54945.herokuapp.com
```

# Installation

Clone the application from the link `https://github.com/kelvin-otieno/politico-api.git` or simply download the zipped file and extract to your computer.

# Run

    Install postgress db to your local machine
    Create a database on postgress and update the DATABASE_URL variable in the .env file with the correct details
    Navigate to the root of the project
    Install all the requirements `pip install -r requirements.txt`
    export all the environment variables `source .env`
    Run the application `python run.py`

# Testing

To test, while on the root folder, run `pytest -v tests/` or simply navigate to the tests folder and run `pytest -v`

# Endpoints

| Endpoint                        |      Functionality      | Method |
| ------------------------------- | :---------------------: | ------ |
| /api/v2/parties/                |     Create a party      | POST   |
| /api/v2/parties/                |     Get all parties     | GET    |
| /api/v2/parties/`<id>`          |  Get a specific party   | GET    |
| /api/v2/parties/`<id>`          |  Edit a specific party  | PUT    |
| /api/v2/parties/`<id>`          | Delete a specific party | DELETE |
| /api/v2/offices/                |    Create an office     | POST   |
| /api/v2/offices/`<id>`          |  Get a specific office  | GET    |
| /api/v2/offices/`<id>`          |     Edit an office      | PUT    |
| /api/v2/offices/`<id>`          |    Delete an office     | DELETE |
| /api/v2/offices/                |     Get all offices     | GET    |
| /api/v2/auth/signup/            |      Create a user      | POST   |
| /api/v2/auth/login/             |      Login a user       | POST   |
| /api/v2/office/`<id>`/register/ |  Register a candidate   | POST   |
| /api/v2/votes/                  |          Vote           | POST   |
| /api/v2/office/`<id>`/result/   |       Count votes       | POST   |
| /api/v2/office/                 |   Get all candidates    | GET    |
| /api/v2/auth/                   |      Get all users      | GET    |
| /api/v2/auth/reset              |     Reset password      | POST   |
| /api/v2/petitions/              |    Get all petitions    | GET    |
| /api/v2/petitions/              |    Create a petition    | POST   |

# Project Management

[Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2241865)

# Project Documentation

[Politico API Documentation](https://politico14.docs.apiary.io/)

# Licence

© Kelvin Otieno
