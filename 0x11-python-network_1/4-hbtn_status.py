#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
""" script that fetches https://intranet.hbtn.io/status """

import requests

if __name__ == "__main__":
        r = requests.get('https://intranet.hbtn.io/status')
        # print(r.text)
        print("Body Response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
