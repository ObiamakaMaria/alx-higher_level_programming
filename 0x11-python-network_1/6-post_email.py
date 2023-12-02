#!/usr/bin/python3
""" This script sends POST request with an email as prarameter"""

if __name__ == "__main__":
    import requests
    import sys
    c_option = sys.argv

    param = {'email': c_option[2]}
    resp = requests.post(c_option[1], param=param)
    print(resp.text)
