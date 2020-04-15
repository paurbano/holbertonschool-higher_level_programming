#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
""" script that fetches https://intranet.hbtn.io/status """


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        answer = response.read()
        print("Body response:")
        print("    - type: {}".format(type(answer)))
        print("    - content: {}".format(answer))
        print("    - utf8 content: {}".format(answer.decode('utf-8')))
