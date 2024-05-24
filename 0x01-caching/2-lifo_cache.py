#!/usr/bin/env python3
"""LIFO caching module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class
        Args:
            BaseCaching (class): Base caching class
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    del self.cache_data[self.queue[-1]]
                    print(f"DISCARD: {self.queue[-1]}")
                    self.queue.pop(-1)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
