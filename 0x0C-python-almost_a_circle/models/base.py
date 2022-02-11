#!/usr/bin/python3
"""class base"""
import json


class Base:
    """attribuites"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object in file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for obj in range(len(list_objs)):
                list_dic.append(list_objs[obj].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """String to dictionary"""
        if not json_string:
            return []
        return json.loads(json_string)
