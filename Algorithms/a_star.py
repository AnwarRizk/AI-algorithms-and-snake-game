# A* algorithm

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)]
}

H_table = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost, last_node

def a_star(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_f_cost) # sort the queue by the cost of the paths, if the cost is the same then sort by the last node alphabetically
        path = queue.pop(0) # get the path with the lowest cost
        node = path[-1][0] # get the last node in the path
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

solution = a_star(graph, 'S', 'G')
print('A*:', solution)
print('Cost:', path_f_cost(solution)[0])