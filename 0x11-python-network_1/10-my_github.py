#!/usr/bin/python3
""" This script GET properties from mail"""

if __name__ == '__main__':
    import requests
    import sys
    headers = {}
    headers['Authorization'] = '{} {}'.format(sys.argv[0], sys.argv[1])
    e = requests.get('https://api.github.com/users/{}'
                     .format(sys.argv[1]), headers=headers)
    print(e.json().get('id'))
