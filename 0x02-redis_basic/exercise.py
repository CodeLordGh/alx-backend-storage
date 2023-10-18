#!/usr/bin/env python3

from typing import Union, Callable
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

    def get(self, key: str, fn: Callable[[bytes], Union[str, int]] = None) -> Union[str, int, None]:
        """Retrieves the data associated with the given key from Redis.

        Args:
            key: The key of the data to be retrieved.
            fn: A callable to convert the data back to the desired format.

        Returns:
            The data associated with the given key, or `None` if the key does
            not exist.
        """

        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """Retrieves the string associated with the given key from Redis.

        Args:
            key: The key of the string to be retrieved.

        Returns:
            The string associated with the given key, or `None` if the key does
            not exist.
        """

        return self.get(key, fn=bytes.decode)

    def get_int(self, key: str) -> int:
        """Retrieves the integer associated with the given key from Redis.

        Args:
            key: The key of the integer to be retrieved.

        Returns:
            The integer associated with the given key, or `None` if the key does
            not exist.
        """

        return self.get(key, fn=int)
