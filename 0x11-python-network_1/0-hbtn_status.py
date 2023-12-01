#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:$")
        print("    - type: {}".format(type(content)), "$")
        print("    - content: {}".format(content), "$")
        print("    - utf8 content: {}".format(utf8_content), "$")
