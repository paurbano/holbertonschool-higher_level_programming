#!/usr/bin/python3
#  sends a POST request to the passed URL with the email as a parameter,
# and displays the body of the response
""" script that fetches header """


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    parameters = {}
    parameters['email'] = sys.argv[2]
    data = urllib.parse.urlencode(parameters)
    data = data.encode()
    # fullurl = url + '?' + data
    # print(data)
    with urllib.request.urlopen(url, data) as response:
        answer = response.read()
        print(answer.decode('utf-8'))
