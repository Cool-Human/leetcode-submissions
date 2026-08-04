"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newMap = {}
        queue = deque([node])
        newMap[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbour in curr.neighbors:
                if neighbour not in newMap:
                    newMap[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                newMap[curr].neighbors.append(newMap[neighbour])
        
        return newMap[node]