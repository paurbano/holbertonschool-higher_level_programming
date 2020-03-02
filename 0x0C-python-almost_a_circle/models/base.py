#!/usr/bin/python3
""" Module Base """
import json


class Base:
    """ Class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON representation of an object """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON representation of an object to text file"""
        namefile = cls.__name__ + ".json"
        rep_list = []
        if list_objs is not None and list_objs != []:
            for item in list_objs:
                repre = cls.to_dictionary(item)
                # rep_list.append(cls.to_json_string(repre))
                rep_list.append(repre)

        with open(namefile, "w", encoding="UTF-8") as f:
            # json.dump(rep_list, f)
            f.write(cls.to_json_string(rep_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string """
        empty_list = []
        if json_string is None:
            return empty_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set: """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            text = []
            with open(filename, 'r') as f:
                text = cls.from_json_string(f.read())
                for obj in text:
                    instances.append(cls.create(**obj))
        except FileNotFoundError:
            instances = []

        return instances
