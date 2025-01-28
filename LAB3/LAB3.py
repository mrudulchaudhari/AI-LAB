graph = {
    'A': {'B': 5, 'D': 10},
    'B': {'C': 4, 'F': 15},
    'C': {'E': 8},
    'D': {'F': 11},
    'E': {},
    'F': {'E': 4}
}

def ucs(graph, start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        # Get lowest cost path
        cost, path = min(queue)
        queue.remove((cost, path))
        node = path[-1]

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for next_node, step_cost in graph[node].items():
            if next_node not in visited:
                queue.append((cost + step_cost, path + [next_node]))

    return None, None

# Find path
path, cost = ucs(graph, 'A', 'E')
print(f"Path: {path}")
print(f"Cost: {cost}")