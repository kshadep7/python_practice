class Graph:
  def __init__(self, adjList = {}):
    # the adjacency list is of type Dict[int,List[int]]
    self.adjList = adjList

graph = Graph()
graph.adjList = {
  5 : [8, 1, 12],
  8 : [5, 12, 14, 4],
  12 : [5, 8, 14],
  14 : [8, 12, 4],
  4 : [8, 14],
  1 : [5, 7],
  7 : [1, 16],
  16 : [7]
}

def bfs(graph, root):
    visited = set()
    res = helper(graph, root, visited)
    print(res)

def helper(graph, root, visited):
    res = []
    queue = []
    queue.append(root)
    visited.add(root)
    while len(queue) != 0:
       node = queue.pop(0)
       res.append(node)
       for neighbor in graph.adjList[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return res

if __name__=='__main__':
   bfs(graph, 5)