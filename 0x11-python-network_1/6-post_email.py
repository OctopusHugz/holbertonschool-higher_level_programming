#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
