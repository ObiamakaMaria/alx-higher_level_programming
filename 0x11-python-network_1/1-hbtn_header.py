#!/usr/bin/python3
""" This script displays the value of the X-Request-Id
    variable in the response header.
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as resp:
            # Retrieve the X-Request-Id header from the response
            x_request_id = resp.getheader("X-Request-Id")

            # Display the value of the X-Request-Id variable
            print("X-Request-Id:", x_request_id)

    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL -", e.reason)
