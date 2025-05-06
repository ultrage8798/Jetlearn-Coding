from collections import defaultdict

class Graph():
    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.V = verticies

    def ae(self, u, v):
        self. graph[u].append(v)

    def icu(self, v, visited, rs)
        visited[v] = True
        rs[v] = True
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.icu(neighbor, visited, rs) == True:
                    return True
            elif rs[neighbor] == True:
                return True:
        rs[v] = False
        return False

    def ic(self):
        visited = [False] * (self.V + 1)
        rs = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.icu(node, visited, rs) == True:
                    return True
        return False
    
g = Graph(4)
g.ae(0, 1)
g.ae(0, 2)
g.ae(1, 2)
g.ae(2, 0)
g.ae(2, 3)
g.ae(3, 3)
if g.ic() == 1:
    print("Graph has a cycle.")
else:
    print("Graph has no cycle.")