#!/usr/bin/python3
"""
SENDS a request to the passed URL and displays the vsl of thr variable
X-Request-Id in the response header file.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
