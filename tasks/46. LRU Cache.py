# Task description:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to
# the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


# Hash Map with a Doubly Linked List (or Python's Native Ordered Dictionary).
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        """Initializes the LRU cache with positive size capacity."""
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """Returns the value of the key if it exists, otherwise returns -1."""
        if key not in self.cache:
            return -1

        # Move the accessed key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """Updates or inserts the key-value pair, evicting the oldest if capacity is exceeded."""
        if key in self.cache:
            # Update value and refresh its currency placement
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Check capacity before insertion
            if len(self.cache) >= self.capacity:
                # popitem(last=False) removes and returns the first (oldest) key-value pair (FIFO)
                self.cache.popitem(last=False)

            # Insert the new element
            self.cache[key] = value


if __name__ == "__main__":
    # Initialize cache with a capacity of 2 slots
    lru = LRUCache(2)

    lru.put(1, 1)  # Cache is {1: 1}
    lru.put(2, 2)  # Cache is {1: 1, 2: 2}

    print(f"Get key 1: {lru.get(1)}")  # Returns 1. Cache becomes {2: 2, 1: 1}

    lru.put(3, 3)  # Evicts key 2! Cache becomes {1: 1, 3: 3}

    print(f"Get key 2: {lru.get(2)}")  # Returns -1 (not found)

    lru.put(4, 4)  # Evicts key 1! Cache becomes {3: 3, 4: 4}

    print(f"Get key 1: {lru.get(1)}")  # Returns -1 (not found)
    print(f"Get key 3: {lru.get(3)}")  # Returns 3
    print(f"Get key 4: {lru.get(4)}")  # Returns 4


# Time Complexity: O(1) constant average execution time for both get and put operations. Hash map dictionary key
# mapping takes constant time, and re-linking pointers inside an OrderedDict to shift or pop items executes
# in true O(1) time.
# Space Complexity: O(C) auxiliary space, where C is the maximum capacity of the cache data structure.
# The internal storage allocation scales linearly based entirely on the target capacity parameter constraint.
