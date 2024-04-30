#!/usr/bin/env python3
"""module 9"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value

    mongo_collection.insert_one(my_dict)
