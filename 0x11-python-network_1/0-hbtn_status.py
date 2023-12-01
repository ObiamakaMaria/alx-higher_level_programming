#!/usr/bin/python3
""" This file gets the content of the URL given programmatically """

if __name__ == "__main__":
    from urllib import request

    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:$")
        print("    - type: {}".format(type(content)), "$")
        print("    - content: {}".format(content), "$")
        print("    - utf8 content: {}".format(utf8_content), "$")
