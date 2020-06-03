#!/usr/bin/python3
"""This module adds all command line arguments to a Python list"""
from sys import argv
from os.path import exists
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
args_list = []
for args in argv:
    if not exists("add_item.json"):
        save_to_json_file(args_list, "add_item.json")
    else:
        if args[0] != ".":
            second_list = load_from_json_file("add_item.json")
            second_list.append(args)
            save_to_json_file(second_list, "add_item.json")
