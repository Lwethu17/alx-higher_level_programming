#!/usr/bin/python3
"""
Sends a POST REQUEST to the passed URL withe the emails as a param,
and then displays the body in response (decoded onto utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
