#DLS

DEPTH_LIMIT = 2
GOAL_NODE = "J"
START_NODE = "S"
graph = {
    "S" : ["A", "B"],
    "A" : ["C", "D"],
    "B" : ["I", "J"],
    "C" : ["E", "F"],
    "D" : ["G"],
    "I" : ["H"],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
    "J": [],
}

visited = [START_NODE]
def DLS(start, goal, depth_limit):
  if start == goal:
    return True
  if depth_limit <= 0:
    return False #Return False instead of string
  for neighbour in graph[start]:
    if neighbour not in visited:
      visited.append(neighbour)
      if DLS(neighbour, goal, depth_limit-1):
        return True

  return False

if DLS(START_NODE, GOAL_NODE, DEPTH_LIMIT):
  print("Found")
  print(visited)
else:
  print("Not found")