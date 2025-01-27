# BFS and DFS
#BFS

graph = {
    'A':['B', 'C', 'D'],
    'B':['E','F'],
    'C':['G'],
    'D':['H'],
    'E': [],
    'F':[],
    'G': [],
    'H':[]
}

visited = []
queue = []
START_NODE = "A"

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s, end = " ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("BFS Traversal")
bfs(visited, graph, START_NODE)
print("\n")


#dfs
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

print("DFS traversal")
dfs(visited, graph, START_NODE)