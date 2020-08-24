#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
