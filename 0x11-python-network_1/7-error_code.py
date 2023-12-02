#!/usr/bin/python3
""" This script shows a URL's Error code using status code"""

if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    if (resp.status_code >= 400):
        print('Error code: {}'.format(resp.status_code))
    else:
        print(resp.text)
