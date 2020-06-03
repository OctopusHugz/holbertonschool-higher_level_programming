#!/usr/bin/python3
"""This module implements the to_json_string function"""
import json


def from_json_string(my_str):
    """This function returns the Python object represented
by a JSON string"""
    return json.loads(my_str)
