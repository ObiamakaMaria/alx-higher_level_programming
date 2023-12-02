#!/usr/bin/python3
"""
This script GETS the specified URL & displays the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://alx-intranet.hbtn.io/status"

    try:
        resp = requests.get(url)

        print("Body response:")
        print("    - type: {}".format(type(resp.text)))
        print("    - content: {}".format(resp.text))

    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
