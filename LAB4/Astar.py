from heapq import heappush, heappop

def a_star_search(graph, start, goal, heuristics):
   """
   A* search algorithm implementation.
   
   Args:
       graph (dict): Graph with nodes and edge costs
       start (str): Start node
       goal (str): Goal node 
       heuristics (dict): Heuristic values for nodes
   
   Returns:
       tuple: (path, total_cost) where path is list of nodes and total_cost is sum of edge costs
   """
   open_set = [(heuristics[start], start)]
   closed_set = set()
   g_cost = {start: 0}
   f_cost = {start: heuristics[start]}
   parents = {start: None}
   
   while open_set:
       current_f, current = heappop(open_set)
       
       if current == goal:
           path = []
           while current:
               path.append(current)
               current = parents[current]
           path = path[::-1]
           return path, g_cost[goal]
           
       closed_set.add(current)
       
       for neighbor, edge_cost in graph[current].items():
           if neighbor in closed_set:
               continue
               
           tentative_g = g_cost[current] + edge_cost
           
           if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
               parents[neighbor] = current
               g_cost[neighbor] = tentative_g
               f_cost[neighbor] = tentative_g + heuristics[neighbor]
               heappush(open_set, (f_cost[neighbor], neighbor))
               
   return None, None

graph = {
   'A': {'B': 1, 'C': 2, 'H': 7},
   'B': {'D': 4, 'E': 6},
   'C': {'F': 3, 'G': 2},
   'D': {'E': 7, 'H': 1},
   'E': {'H': 1},
   'F': {'H': 1},
   'G': {'H': 2},
   'H': {}
}

heuristics = {
   'A': 5, 'B': 3, 'C': 4,
   'D': 2, 'E': 6, 'F': 3,
   'G': 1, 'H': 0
}

path, cost = a_star_search(graph, 'A', 'E', heuristics)
if path:
    print(f"Path found: {" -> ".join(path)}")
    print(f"Cost: {cost}")
else:
    print("Not found")