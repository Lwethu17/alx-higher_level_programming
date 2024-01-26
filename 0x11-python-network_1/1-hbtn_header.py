#!/usr/bin/python3
"""
Shows the value of the X-Request-Id variable,
that is found in the header as response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
