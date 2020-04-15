#!/usr/bin/python3
#  takes in a URL, sends a request to the URL and displays
# the body of the response (decoded in utf-8).

""" manage urllib.error.HTTPError exceptions and print:
     Error code: followed by the HTTP status code """


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        try:
            answer = response.read()
            print(answer.decode('utf-8'))
        except HTTPError as e:
            print('Error code: ', e.code)
