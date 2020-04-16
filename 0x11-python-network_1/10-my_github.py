#!/usr/bin/python3
#  sends a request to the URL and displays the value of
# the variable X-Request-Id in the response header
""" script that fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    if len(sys.argv) > 1:
        user = sys.argv[1]
        pwd = sys.argv[2]

    r = requests.get(url, auth=(user, pwd))
    json = r.json()
    print("{}".format(json.get('id')))
