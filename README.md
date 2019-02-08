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

# Installation

Clone the application from the link `https://github.com/kelvin-otieno/politico-api.git` or simply download the zipped file and extract to your computer.

# Run

Navigate to the root of the project then from the terminal execute `python run.py`

# Testing

To test, while on the root folder, run `pytest -v tests/` or simply navigate to the tests folder and run `pytest -v`

# Endpoints

## Creating a party `POST`

`/api/v1/parties/`

## Editing a party `PUT`

`/api/v1/parties/<id>`

## Deleting a party `DELETE`

`/api/v1/parties/<id>`

## Getting all parties `GET`

`/api/v1/parties/`

## Getting a single party `GET`

`/api/v1/parties/<id>`

## Creating an office `POST`

`/api/v1/offices/`

## Getting all offices `GET`

`/api/v1/offices/`

## Getting a single office `POST`

`/api/v1/offices/<id>`

# Licence

© Kelvin Otieno
