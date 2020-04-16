#!/usr/bin/python3
"""
This script shows the commits of a repository of a user
"""
import requests
from sys import argv

if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        argv[1], argv[2])
    rest = requests.get(link)

    if "json" not in rest.headers.get('content-type'):
        print("Not a valid JSON")
    data = rest.json()
    values = 0
    for rest in data:
        if values > 9:
            break
        print(rest.get('sha') + ': ' +
              rest.get('commit').get('author').get('name'))