import requests
from couchbase.bucket import Bucket
__author__ = 'zjf'


def send_simple_message(username):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc140f8236f954551bc5f270901158c43.mailgun.org/messages",
        auth=("api", "key-df9ae46da72fb2eb9c377dfa26664014"),
        data={"from": "Excited User <mailgun@sandboxc140f8236f954551bc5f270901158c43.mailgun.org>",
              "to": [username],
              "subject": "Welcome to NewsBomb",
              "text": "Testing some Mailgun awesomness!"})

def usernameIsValue(username):
    print username
    try:
        bucket = Bucket('couchbase://localhost/default')
        rv = bucket.get(username)
        if rv is not None:
            return True

    except Exception as e:
        print "not found"
        send_simple_message(username)

    #print rv["value"]
    #print rv.value
    # getUsernameJson = json.loads(username)
    #getUsername = username["username"]


#if __name__ == '__main__':
#   send_simple_message("max.meng@appartner.cn")



