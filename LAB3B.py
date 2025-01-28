graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J", "K"],
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
    """
    Depth-limited search implementation
    
    Args:
        node: Current node being explored
        goal: Target node we're searching for
        depth_limit: Maximum depth to search
        path: List to keep track of nodes visited
        
    Returns:
        bool: True if goal is found within depth limit, False otherwise
    """
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
    """
    Iterative deepening depth-first search implementation
    
    Args:
        start: Starting node
        goal: Target node
        max_depth: Maximum depth to search
        
    Returns:
        tuple: (bool, list) - (True if goal found, path taken)
    """
    for depth in range(max_depth + 1):
        path = [start]
        if dls(start, goal, depth, path):
            return True, path
    return False, path

START_NODE = "A"
GOAL_NODE = "R"
MAX_DEPTH = 4

found, path = iddfs(START_NODE, GOAL_NODE, MAX_DEPTH)
print(f"Path found: {found}")
print(f"Path taken: {' -> '.join(path)}")