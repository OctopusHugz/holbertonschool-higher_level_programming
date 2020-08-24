#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    import requests
    from sys import argv
    repo = argv[1]
    owner = argv[2]
    response = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(owner, repo))
    for commit in response.json()[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit["commit"]["author"].get("name")))
