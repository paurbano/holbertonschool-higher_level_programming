#!/usr/bin/python3
#  sends a request to the URL and displays the value of
# the variable X-Request-Id in the response header
""" script that fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error Code: {}".format(r.status_code))
    else:
        print(r.text)
