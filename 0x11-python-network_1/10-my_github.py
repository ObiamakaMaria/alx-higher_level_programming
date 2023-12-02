#!/usr/bin/python3
"""This script uses the GitHub API to display your user id."""
if__name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

        username = sys.argv[1]
        token = sys.argv[2]

        url = "https://api.github.com/user"

    try:
        resp = requests.get(url, auth=(username, token))

        if resp.status_code == 200:
            user_id = resp.json()['id']
            print("Your GitHub user id is:", user_id)
        else:
            print("Error: No info. Status Code:", resp.status_code)

    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
