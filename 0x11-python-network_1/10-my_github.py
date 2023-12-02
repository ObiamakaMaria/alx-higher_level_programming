#!/usr/bin/python3
"""
Uses the GitHub API to display your user id.
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

        username = sys.argv[1]
        token = sys.argv[2]

        url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))

        if response.status_code == 200:
            user_id = response.json()['id']
            print("Your GitHub user id is:", user_id)
        else:
            print("Error: No info. Status Code:", response.status_code)

    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
