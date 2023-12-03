#!/usr/bin/python3
"""This GETS the URL & displays the response."""

if __name__ == "__main__":
    import requests
    re = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(re.text)))
    print('\t- content: {}'.format(re.text))
