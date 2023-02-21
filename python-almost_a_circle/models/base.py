#!/usr/bin/python3
"""
Module Name: base

Module Description:
This module contains only one Class

Module Classes:
- Base

Module Attributes:
- None
"""
import json
import os


class Base:
    """
    The Base class is a simple class for generating unique IDs.

    Attributes:
        __nb_objects (int): A class variable that keeps track of
                            the number of objects created.

    Methods:
        __init__(self, id=None): Initializes a new instance of
                                 the Base class with a unique ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class with a unique ID.

        Args:
            id (int, optional): An optional ID that can be assigned
                                to the instance. If None, the instance
                                is assigned a unique ID generated by the class.

        Returns:
            None.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Parameters:

        list_dictionaries: A list of dictionaries to be converted to a JSON string.
        Returns:

        A JSON string representation of the input list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs) -> None:
        """
        Writes the JSON string representation of a list of Base instances to a file.

        Parameters:

        cls: The class of the Base instance.
        list_objs: A list of Base instances to be saved.
        """
        filename = f"{cls.__name__}.json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        "later"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        "later"
        try:
            filename = f"{cls.__name__}.json"

            with open(filename, mode="r", encoding="utf-8") as f:
                return_value = json.load(f)

            value = cls.__init__(return_value)
            
            return value
        except Exception as e:
            return []
