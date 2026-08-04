from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        self.routeMap = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        if src != dst:
            self.routeMap[src].add(dst)
            if dst not in self.routeMap:
                self.routeMap[dst] = set()

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.routeMap and dst in self.routeMap[src]:
            self.routeMap[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst: return True
        queue = deque([src])
        visited = {src}

        while queue:
            curr = queue.popleft()
            for neighbour in self.routeMap[curr]:
                if neighbour == dst:
                    return True
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        return False