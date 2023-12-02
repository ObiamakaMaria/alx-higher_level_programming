#!/usr/bin/python3
""" Sends a POST request to a URL & response is displayed
    accordig to requirement
"""
if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        resp = requests.post(url, data=data)

        try:
            json_data = resp.json()
            if json_data:
                print("[{}] {}".format(json_data['id'], json_data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
