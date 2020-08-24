#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    import urllib
    from urllib import request
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {:d}".format(e.code))
