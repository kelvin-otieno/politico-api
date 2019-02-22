import re


def isValidEmail(email):
    pattern = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    if not re.match(pattern, email):
        return False
    else:
        return True


def isValidPhoneNumber(phoneNumber):
    if phoneNumber.startswith('07') and len(phoneNumber) == 10 and not phoneNumber.isalpha():
        return True
    else:
        return False


def isValidPassword(password):
    if len(password) < 7:
        return False
    else:
        return True


def isValidPassport(passportUrl):
    if passportUrl.startswith('https://') or passportUrl.startswith('http://'):
        return True
    else:
        return False


def isValidName(names):
    for name in names:
        if re.search('\d', name):
            return False
    return True
