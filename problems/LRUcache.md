## 📦 LRU Cache Implementation (Python)

This document explains a complete Python implementation of an **LRU (Least Recently Used) Cache**, using a combination of:

### 🔧 Data Structures Used:

#### 1. **HashMap (`self.cache`)**
- Stores keys and references to their corresponding nodes in the linked list.
- Allows **O(1)** access for `get()` and `put()` operations.

#### 2. **Doubly Linked List**
- Maintains the order of usage.
- **Most Recently Used (MRU)** items go to the **right end**.
- **Least Recently Used (LRU)** items are at the **left end**.
- Dummy nodes `left` and `right` are used to simplify edge cases (no need to check for empty list when inserting/removing).

---

### 🧠 Core Idea

- On every `get()` or `put()`:
  - Move the accessed/updated node to the **right end** (MRU).
- If the cache exceeds capacity:
  - Remove the node just after the `left` dummy — that's the **LRU item**.

---

## 🧾 Code with Comments

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap: key -> node

        self.left = Node(0, 0)   # Dummy LRU end
        self.right = Node(0, 0)  # Dummy MRU end

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Removes a node from the doubly linked list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # Inserts a node right before the right (MRU end)
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])     # Detach from current position
            self.insert(self.cache[key])     # Re-insert at MRU position
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])     # Remove old version if key exists

        self.cache[key] = Node(key, value)   # Create new or updated node
        self.insert(self.cache[key])         # Always insert at MRU position

        if len(self.cache) > self.capacity:
            lru = self.left.next             # LRU node is after dummy left
            self.remove(lru)                 # Remove from DLL
            del self.cache[lru.key]          # Remove from HashMap
```

### 🔄 Visual ABC Example for `remove()`

Imagine a doubly linked list like this:
A <-> B <-> C

Here's what happens step-by-step:
prev = A
nxt = C

Now you call:

```python
remove(B)
A.next = C
C.prev = A
```
We update the pointers:
A <-> C

B is now detached