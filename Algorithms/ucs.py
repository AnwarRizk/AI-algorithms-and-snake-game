# Uniform Cost Search (UCS) algorithm

graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)]
}

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, node # return the total cost and the last node

def ucs(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)  # sort the queue by the cost of the paths, if the cost is the same then sort by the last node alphabetically
        path = queue.pop(0)  # get the path with the lowest cost
        node = path[-1][0]  # get the last node in the path
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            neighbors = graph[node]
            for neighbor, cost in neighbors:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append((neighbor, cost))
                    queue.append(new_path)

solution = ucs(graph, 'S', 'G')
print('UCS:', solution)
print('Cost:', path_cost(solution)[0])
