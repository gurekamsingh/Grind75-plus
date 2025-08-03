# Problem:
# Design a data structure that behaves like an LRU (Least Recently Used) cache.
# It should support the following operations:
# - get(key): Returns the value of the key if it exists, otherwise returns -1.
# - put(key, value): Inserts or updates the value of the key. If the cache exceeds its capacity, it should remove the least recently used item.

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
# Consider the example of removing B from list A B C 
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev  = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node

        node.next = nxt
        node.prev = prev

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Real-World Use:
# Imagine you're building a web browser cache. You want to keep the most recently accessed pages in memory,
# but you also want to remove the least recently used pages when the cache exceeds its capacity.
# This LRUCache implementation helps you manage that efficiently.   
# Time & Space:
# Time: O(1) for both get and put operations
# Space: O(n) where n is the capacity of the cache

# Usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1
lru_cache.put(3, 3) # Evicts key 2  
print(lru_cache.get(2))  # Output: -1 (not found)
lru_cache.put(4, 4)
print(lru_cache.get(1))  # Output: 1