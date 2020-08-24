#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
