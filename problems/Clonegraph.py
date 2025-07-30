# Problem: Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.
# A deep copy means:
# You’re not just pointing to the same old nodes.
# You’re creating completely new nodes, with the same values and connections as the original graph.
# Changes to the original should not affect the copy.

# The trick is: as we traverse the graph, we need to remember which nodes we’ve already cloned, otherwise we’ll:

# Duplicate nodes

# Get stuck in infinite loops due to cycles

# We’ll use:

# BFS or DFS + HashMap
# Where:

# Key: original node

# Value: cloned node

# This way, every time we revisit a node, we check: “Have I already cloned this? If yes, reuse the clone.”

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect nodes (undirected graph)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]




# Main function is this below ;above is the question to test the code
def Clonegraph(node):
    if not node:
         return None
    
#  visited is a dictionary (hashmap)
#  It stores= Key: original node object (e.g., Node(1)); Value: the cloned node object (e.g., Cloned_Node(1))
# This way, every time we see a node we've already copied, we can just reuse its clone — no need to recreate it.
    visited = {}
    
    def dfs(current):
        if current in visited:
            return visited[current]
        
# We’re inside a DFS function that’s trying to clone a graph node and all of its connections.
# We already created a clone of the current node:
        clone = Node(current.val)
        visited[current] = clone

        for neighbor in current.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

# Main function is above


def print_graph(Node):
    visited = set()
    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        print(f"Node: {n.val}, Neighbors: {[neigh.val for neigh in n.neighbors]}")
        for neigh in n.neighbors:
            dfs(neigh)
    dfs(Node)


cloned_node = Clonegraph(node3)

print("Original:")
print_graph(node3)

print("\nCloned:")
print_graph(cloned_node)
