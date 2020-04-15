#!/usr/bin/python3
#  sends a request to the URL and displays the value of
# the variable X-Request-Id in the response header
""" script that fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
        url = sys.argv[1]
        payload = {'email': sys.argv[2]}
        r = requests.post(url, data=payload)
        print(r.text)
