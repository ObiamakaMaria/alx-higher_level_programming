#!/usr/bin/python3
"""
   This script sends a request to the given URL and displays  the
   response, it handles urllib.error.HTTPError exceptions and prints
   the HTTP status code in case of an error.
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode('utf-8')
            print(content)

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
        sys.exit(1)
