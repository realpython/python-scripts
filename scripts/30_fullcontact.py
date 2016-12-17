import os
import sys
import requests

"""

1. pip install requests
2. Obtain an API key: https://www.fullcontact.com/developer/pricing/

Example usage:

$ python 30_fullcontact.py email SOME@EMAIL.COM
$ python 30_fullcontact.py twitter TWITTER_HANDLE
"""


# constants

API_KEY = os.environ.get('FULLCONTACT_API_KEY')
BASE_URL = 'http://api.fullcontact.com/v2/person.json'


# helpers

def get_arguments():
    if len(sys.argv) is 3:
        return {
            'media': sys.argv[1],
            'user_info': sys.argv[2]
        }
    else:
        print('Specify at least 1 argument')
        sys.exit()


def call_api(contact):
    url = BASE_URL + '?{0}={1}&apiKey={2}'.format(
        contact['media'], contact['user_info'], API_KEY)
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return "Sorry, no results found."


# main

if __name__ == "__main__":
    media = get_arguments()
    print(call_api(media))
