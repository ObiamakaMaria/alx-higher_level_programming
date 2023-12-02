#!/usr/bin/python3
""" This script displays the value of the variable X-Request-Id """

if __name__ == "__main__":
    import requests
    import sys

    option = sys.argv1
    resp = requests.get(option[1])
    print(resp.headers.get('X-Request-Id'))
