from heapq import heappush, heappop

def greedy_best_search(graph, start, goal, heuristics):
   """
   Performs Greedy Best-First Search to find path from start to goal node.
   
   Args:
       graph (dict): Graph representation as adjacency list
       start (str): Starting node
       goal (str): Goal node 
       heuristics (dict): Heuristic values for each node
   
   Returns:
       list: Path from start to goal if found, None otherwise
   """
   pq = [(heuristics[start], start, [start])]
   visited = set()
   
   while pq:
       h_val, current, path = heappop(pq)
       
       if current == goal:
           return path
           
       if current not in visited:
           visited.add(current)
           
           for neighbor in graph[current]:
               if neighbor not in visited:
                   new_path = path + [neighbor]
                   heappush(pq, (heuristics[neighbor], neighbor, new_path))
   
   return None

graph = {
   'A': ['B', 'C'],
   'B': ['D', 'E'],
   'C': ['F', 'G'],
   'D': ['H'],
   'E': ['H'], 
   'F': ['H'],
   'G': ['H'],
   'H': []
}

heuristics = {
   'A': 13, 'B': 12, 'C': 4,
   'D': 7,  'E': 3,  'F': 8,
   'G': 2,  'H': 0
}

path = greedy_best_search(graph, 'A', 'H', heuristics)
if path:
    print(f"Path found: {" -> ".join(path)}")
else:
    print("Not found")