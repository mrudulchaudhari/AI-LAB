# Iterative Deepening

graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": ["L"],
    "H": ["M", "N"],
    "I": [],
    "J": [],
    "K": ["O", "P"],
    "L": ["R"],
    "M": [],
    "N": ["S"],
    "O": [],
    "P": [],
    "R": [],
    "S": []
}

def dls(node, goal, depth_limit, path):
    if node == goal:
        return True
    
    if depth_limit <= 0:
        return False
    
    for neighbor in graph[node]:
        path.append(neighbor)
        if dls(neighbor, goal, depth_limit - 1, path):
            return True    
    return False

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = [start]
        if dls(start, goal, depth, visited):
            return True, visited
    return False, visited

# Test
START_NODE = "A"
found, path = iddfs(START_NODE, "R", 4)
print(f"Path taken: {"->".join(path)}")