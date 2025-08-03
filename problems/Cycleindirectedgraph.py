# Problem:
# Given a directed graph, determine if it contains a cycle. 
# A cycle exists if we can return to a node that is already in the current path of exploration.   

# Approach:
# Use Depth First Search (DFS) to traverse the graph.
# Maintain a visited set to track nodes that have been fully explored.
# Use a recursion stack to track nodes in the current path of exploration.
# If we encounter a node that is already in the recursion stack, a cycle exists. 


def hascycle(graph):
    visited = set()
    recstack = set()

    def dfs(node):
        if node in recstack:
            return True  # Cycle detected, we exit the loop
        if node in visited: # we have already visited this node, so we skip it go to next line
            return False
        
        visited.add(node)
        recstack.add(node)

        for neighbour in graph.get(node, []):
            if dfs(neighbour):
                return True   # Cycle detected

        recstack.remove(node) # If there is no neighbour of the current node it exits the loop.
        return False
    
    for node in graph: # Iterate through each node in the graph
        # If the node has not been visited, we start a DFS from it
        if node not in visited:
            if dfs(node): # Cycle detected
                return True 
    return False

# Example usage:
graph = {
    1: [2],
    2: [3, 8],
    3: [4, 7],
    4: [6],
    5: [4],
    6: [],
    7: [5],
    8: [9],
    9: [10],
    10: [8]
}

print(hascycle(graph))  # Output: True (because of the cycle 8 -> 9 -> 10 -> 8)