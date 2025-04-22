class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def CE(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def BFS(self, source):
        visited = [False]*self.n
        res = []
        q = []
        q.append(source)
        visited[source] = True
        while len(q) > 0:
            s = q.pop(0)
            res.append(s)

            for node in self.adj[s]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True

        return res
    
graph = Graph(4)
graph.CE(1,2)
graph.CE(1,3)
graph.CE(2,4)

print(graph.BFS(0))