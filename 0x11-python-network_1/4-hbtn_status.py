#!/usr/bin/python3
""" Fetches the URL with request package."""
import requests

if __name__ == "__main__":
    m = requests.get('https://alx-intranet.hbtn.io/status')
    t = m.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
