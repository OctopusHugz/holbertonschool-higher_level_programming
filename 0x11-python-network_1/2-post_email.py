#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode())
