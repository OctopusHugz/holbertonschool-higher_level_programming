#!/usr/bin/python3
"""This module creates a python script to interact with a url"""
if __name__ == "__main__":
    import requests
    from sys import argv
    rj = {}
    try:
        q = argv[1]
    except:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        rj = response.json()
        if len(rj) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(rj.get("id"), rj.get("name")))
    except:
        print("Not a valid JSON")
