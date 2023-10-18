#!/usr/bin/env python3
"""
script
"""
from typing import Union
import uuid
import redis

class Cache:
    """A class for caching data in Redis.

    Attributes:
        _redis: A Redis client instance.
    """

    def __init__(self):
        """Initializes a new Cache instance.

        Flushes the Redis database using `flushdb`.
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in Redis and returns a random key.

        Args:
            data: The data to be stored.

        Returns:
            A random key that can be used to retrieve the data from Redis.
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
