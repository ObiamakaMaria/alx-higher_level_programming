#!/usr/bin/python3
"""This script GETS the specified URL & displays the response."""

if __name__ == "__main__":
    import requests
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(resp.texp)))
    print('\t- content: {}'.format(resp.text))
