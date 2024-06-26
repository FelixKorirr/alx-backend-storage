#!/usr/bin/env python3
'''module 10'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a school document based on name'''
    mongo_collection.update_many(
        { 'name' : name }, { '$set': { 'topics' : topics } }
    )
