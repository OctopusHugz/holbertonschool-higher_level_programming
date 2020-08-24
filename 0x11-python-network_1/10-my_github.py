#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
from requests.models import HTTPBasicAuth
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(
        argv[1], argv[2]))
    print(response.json().get("id"))
