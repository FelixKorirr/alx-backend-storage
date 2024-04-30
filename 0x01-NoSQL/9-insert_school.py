#!/usr/bin/env python3
"""module 9"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value

    mongo_collection.insert_one(my_dict)

    new_document = mongo_collection.find_one({})
    id_of_document = new_document['_id']

    return id_of_document
