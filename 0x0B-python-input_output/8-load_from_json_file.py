#!/usr/bin/python3
"""This module implements the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """This function loads a JSON object from a file filename"""
    with open(filename) as fp:
        text = fp.read()
    return json.loads(text)
