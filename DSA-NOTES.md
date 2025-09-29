## 🌐 What is a Graph?

A **graph** is just a collection of **nodes** (also called *vertices*) connected by **edges**.

### 🧠 Real-life examples:
- **Google Maps**: Cities (nodes) connected by roads (edges)
- **Social Network**: People (nodes) connected by friendships (edges)
- **The Web**: Websites (nodes) linked via hyperlinks (edges)

---

## 📊 Types of Graphs

### ➤ Directed vs Undirected
- **Directed**: Edges have direction (e.g., Twitter followers)
- **Undirected**: Edges go both ways (e.g., Facebook friends)

### ➤ Weighted vs Unweighted
- **Weighted**: Edges have a cost (e.g., time, distance)
- **Unweighted**: All edges are treated the same

### ➤ Cyclic vs Acyclic
- **Cyclic**: Graph contains one or more loops
- **Acyclic**: No cycles (e.g., trees are acyclic)

---

## 🔍 DFS (Depth-First Search)

**Strategy**: Go deep before you go wide.  
You explore one path all the way before backtracking and trying another.

### 🎯 Analogy:
Exploring a maze by following one hallway until you hit a dead end, then backing up.

---

## 🌊 BFS (Breadth-First Search)

**Strategy**: Explore layer by layer, like ripples in water.  
You visit all neighbors of a node before moving to the next level.

### 🎯 Analogy:
Finding the shortest path from one person to another in a social network.

---


## 🔁 Subarrays

A **subarray** is a **contiguous** part of an array.  
Order matters, and the elements must be **next to each other** in the original array.

### ✨ Example:
Given `nums = [1, 2, 3]`  
The possible subarrays are:
- `[1]`, `[2]`, `[3]`
- `[1, 2]`, `[2, 3]`
- `[1, 2, 3]`

### ❌ These are **not** subarrays:
- `[1, 3]` (not contiguous)

### 🔍 Subarrays vs Subsets:
- **Subarray** = must be continuous
- **Subset** = any combination of elements, order doesn't matter, can skip elements

---

## ⛏️ Heaps

A **heap** is a special type of binary tree (or array-based structure) used to quickly access the smallest or largest element. It supports fast insertions and deletions while maintaining a partial ordering of elements.

Heaps are most commonly used in **priority queues**, scheduling, and "Top K" problems.

---

## 🔻 Min-Heap

- The **smallest element** is always at the top (root).
- Every parent node is **less than or equal to** its children.
- In Python, the `heapq` module implements a **min-heap** by default.

### 🧠 Use Case:
- Quickly get the minimum element (like scheduling the shortest job first).
- Maintain the top K **largest** elements by removing the smallest when the heap grows beyond size K.

---

## 🔺 Max-Heap

- The **largest element** is at the top.
- Every parent node is **greater than or equal to** its children.
- Python does not have a built-in max-heap, but you can simulate it using **negative numbers**.

### Example trick:
To push a value into a max-heap:
```python
heapq.heappush(heap, -val)
```

## 🧺 Set (Data Structure)

A **set** is an unordered collection of unique elements.

### 🔑 Key Features:
- No duplicates allowed
- Fast lookups, insertions, and deletions — average **O(1)** time
- Often used to check for existence or to track unique values

### 🧠 Example Use Cases:
- Checking for duplicates in a string or array
- Tracking visited nodes in graph problems
- Sliding window problems (e.g., longest substring without repeating characters)

### ✨ Python Example:
```python
s = set()
s.add('a')
s.add('b')
s.add('a')  # duplicate, will be ignored
print(s)    # Output: {'a', 'b'}
```
## 📚 Stack

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
The last element added is the first one to be removed.

### 🧠 Real-life analogy:

A stack of plates: You add (push) plates on top, and remove (pop) from the top.

### 🔑 Operations:

- Push: Add an element to the top

- Pop: Remove the top element

- Peek/Top: View the top element without removing it

⏱️ Time Complexity:

- Push → O(1)

- Pop → O(1)

- Peek → O(1)

## 🛤️ Queue

A queue is a linear data structure that follows the FIFO (First In, First Out) principle.
The first element added is the first one to be removed.

### 🧠 Real-life analogy:

A line at a movie theater: People join at the back and are served from the front.

### 🔑 Operations:

- Enqueue: Add an element at the rear

- Dequeue: Remove an element from the front

- Peek/Front: View the first element without removing it

⏱️ Time Complexity:

- Enqueue → O(1)

- Dequeue → O(1)

- Peek → O(1)

