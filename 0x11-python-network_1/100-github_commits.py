#!/usr/bin/python3
"""This script displays two names as a response """

if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                      .format(sys.argv[2], sys.argv[1]))
    value = r.json()

    try:
        for x in range(10):
            print("{}: {}".format(
                  value[x].get("sha"),
                  value[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
