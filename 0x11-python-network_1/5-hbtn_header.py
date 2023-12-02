#!/usr/bin/python3
"""
    This script displays the value of the variable X-Request-Id
    in the response header.
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        resp = requests.get(url)

        if 'X-Request-Id' in response.headers:
            x_request_id = resp.headers['X-Request-Id']
            print(x_request_id)
