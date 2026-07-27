class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(src, dst, visited):
            if src == dst:
                return True
            visited.add(src)
            for neighbour in self.graph.get(src, []):
                if neighbour not in visited:
                    if dfs(neighbour, dst, visited):
                        return True
            return False
        return dfs(src, dst, visited)
