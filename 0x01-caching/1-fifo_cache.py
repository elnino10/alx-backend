#!/usr/bin/env python3
"""FIFO caching module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class
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
                    del self.cache_data[self.queue[0]]
                    print(f"DISCARD: {self.queue[0]}")
                    self.queue.pop(0)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
