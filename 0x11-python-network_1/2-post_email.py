#!/usr/bin/python3
"""
   This script sends a POST request to the given URL
   with the email as a parameter and displays the response.
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Encoding the email
    en_data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        with urllib.request.urlopen(url, en_data) as resp:
            content = resp.read().decode('utf-8')

            print(content)

    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL -", e.reason)
