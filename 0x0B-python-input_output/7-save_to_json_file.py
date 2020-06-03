#!/usr/bin/python3
"""This module implements the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes a JSON object to a file filename"""
    with open(filename, "w") as fp:
        fp.write(json.dumps(my_obj))
