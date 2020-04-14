#!/usr/bin/python3

"""
This script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")