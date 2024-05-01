#!/usr/bin/env python3
'''Redis basics'''
import uuid
import redis
from typing import Union


class Cache:
    '''Represents Cache class'''

    def __init__(self):
        '''Initialize Cache class'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]):
        '''Generates random key'''
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
