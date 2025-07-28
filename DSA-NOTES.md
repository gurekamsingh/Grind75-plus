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