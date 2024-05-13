# Breadth First Search (BFS) algorithm

# The graph is represented as an adjacency list
graph = {
    'S': ['A', 'B', 'D'],
    'A': ['C'],
    'B': ['D'],
    'C': ['D', 'G'],
    'D': ['G']
}

def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = [[start]]  # Queue to keep track of paths to explore
    while queue:
        path = queue.pop(0)  # Dequeue the first path from the queue
        node = path[-1]  # Get the last node in the path
        if node not in visited:  # Check if the node has not been visited yet
            if node == goal:  # If the node is the goal node, return the path
                return path
            visited.add(node)  # Mark the node as visited
            neighbors = graph[node]  # Get the neighbors of the current node
            for neighbor in neighbors:  # Iterate over the neighbors
                new_path = list(path)  # Create a new path by copying the current path
                new_path.append(neighbor)  # Append the neighbor to the new path
                queue.append(new_path)  # Enqueue the new path for exploration

# Find a path from 'S' to 'G' using Breadth First Search
solution = bfs(graph, 'S', 'G')
print('BFS:', solution)
