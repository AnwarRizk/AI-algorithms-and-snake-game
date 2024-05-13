# Breadth First Search (BFS) algorithm

# The graph is represented as an adjacency list
graph = {
    'S': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'C': ['D', 'G'],
    'D': ['G']
}

def dfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    stack = [[start]]  # Stack to keep track of the current path
    while stack:
        path = stack.pop()  # Pop the last path from the stack
        node = path[-1]  # Get the last node in the path
        if node not in visited:  # Check if the node has not been visited yet
            if node == goal:  # If the node is the goal node, return the path
                return path
            visited.add(node)  # Mark the node as visited
            neighbors = graph[node]  # Get the neighbors of the current node
            for neighbor in neighbors:  # Iterate over the neighbors
                new_path = list(path)  # Create a new path by copying the current path
                new_path.append(neighbor)  # Append the neighbor to the new path
                stack.append(new_path)  # Push the new path onto the stack

# Find a path from 'S' to 'G' using Depth First Search
solution = dfs(graph, 'S', 'G')
print('DFS:', solution)
