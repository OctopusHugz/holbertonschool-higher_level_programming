#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(html.__class__))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(response.msg))
