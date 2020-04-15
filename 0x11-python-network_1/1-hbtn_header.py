#!/usr/bin/python3
#  displays the value of the X-Request-Id variable
#  found in the header of the response
""" script that fetches header """


if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    # print(url)
    with urllib.request.urlopen(url) as response:
        answer = response.read()
        print(response.info().get('X-Request-Id'))
