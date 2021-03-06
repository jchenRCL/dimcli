#http://docs.dimensions.ai/dsl/1.6.0/api.html

import requests
import time

#   The credentials to be used
login = {'username': 'USR', 'password': 'PSW'}

SERVICE = 'https://app.dimensions.ai/api/'

#   Send credentials to login url to retrieve token. Raise
#   an error, if the return code indicates a problem.
#   Please use the URL of the system you'd like to access the API
#   in the example below.
resp = requests.post(SERVICE + 'auth.json', json=login)
resp.raise_for_status()

#   Create http header using the generated token.
headers = {'Authorization': "JWT " + resp.json()['token']}

#   Execute DSL query.
resp = requests.post(
    SERVICE + 'dsl.json',
    data='search publications return FOR',
    headers=headers)

#   Display raw result
print(resp.json())