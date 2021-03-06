#!/usr/bin/python3
"""This module implements the Base class"""
import json
import os
import csv


class Base:
    """This is the Base class's instantiation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function creates the Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns the JSON string representation of
list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of list_objs
to a file"""
        filename = cls.__name__ + ".json"
        new_list = []
        with open(filename, "w") as fp:
            if list_objs is None:
                fp.write("[]")
            else:
                for objs in list_objs:
                    new_list.append(cls.to_dictionary(objs))
                fp.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """This function returns the list of the JSON string representation"""
        new_list = []
        if json_string is None:
            return new_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set"""
        new_inst = cls.__new__(cls)
        if cls.__name__ == "Rectangle":
            new_inst.__init__(42, 98)
        elif cls.__name__ == "Square":
            new_inst.__init__(42)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """This function returns a list of instances"""
        filename = cls.__name__ + ".json"
        new_list = []
        if not os.path.isfile(filename):
            return new_list
        with open(filename) as fp:
            json_string = fp.read()
        cls_list = cls.from_json_string(json_string)
        for items in cls_list:
            new_inst = cls.create(**items)
            new_list.append(new_inst)
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This functions saves a list of objects to a CSV file"""
        r_fields = ['id', 'width', 'height', 'x', 'y']
        s_fields = ['id', 'size', 'x', 'y']
        filename = cls.__name__ + ".csv"
        new_list = []
        with open(filename, "w") as fp:
            if cls.__name__ == "Rectangle":
                dict_writer = csv.DictWriter(fp, fieldnames=r_fields)
            elif cls.__name__ == "Square":
                dict_writer = csv.DictWriter(fp, fieldnames=s_fields)
            dict_writer.writeheader()
            for objs in list_objs:
                dict_writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This functions loads a list of objects from a CSV file"""
        fields = []
        rows = []
        new_dict = {}
        new_list = []
        key = ""
        filename = cls.__name__ + ".csv"
        with open(filename) as fp:
            reader = csv.reader(fp)
            fields = next(reader)
            for row in reader:
                rows.append(row)
        for row in rows:
            i = 0
            new_dict = new_dict.fromkeys(fields)
            for attr in fields:
                key = fields[i]
                value = row[i]
                new_dict[key] = value
                i += 1
            new_list.append(cls.create(**new_dict))
        return new_list
