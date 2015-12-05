__author__ = 'zjf'


def usernameIsValue(json):
    getUsernameJson = json.loads(json)
    getUsername = getUsernameJson["username"]
    if getUsername == "user":
        return True
    else:
        return False