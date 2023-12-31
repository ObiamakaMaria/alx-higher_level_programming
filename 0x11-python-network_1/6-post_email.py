#!/usr/bin/python3
"""This script sends a POST request with an email as a parameter"""

if __name__ == "__main__":
    import requests
    import sys

    data = {'email': sys.argv[2]}
    resp = requests.post(sys.argv[1], data=data)
    print(resp.text)
