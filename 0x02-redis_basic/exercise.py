#!/usr/bin/env python3
"""Redis basics"""
import uuid
import redis

class Cache:
    """Represents Cache class"""
    def __init__(self):
        """Initialize Cache class"""
        self._redis = redis.Redis()

    def store(self, data):
        """Generates random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    def get(key):
        """Decodes redis data return type
            to desired format"""
        return key.decode('utf-8')
