# Greedy best first search algorithm

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

def path_h_cost(path):
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node

def greedy(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost) # sort the queue by the cost of the paths, if the cost is the same then sort by the last node alphabetically
        path = queue.pop(0) # get the path with the lowest cost
        node = path[-1][0] # get the last node in the path
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            neighbours = graph[node]
            for neighbour, cost in neighbours:
                if neighbour not in visited:
                    new_path = list(path)
                    new_path.append((neighbour, cost))
                    queue.append(new_path)

solution = greedy(graph, 'S', 'G')
print('Greedy:', solution)
print('Cost:', path_h_cost(solution)[0])