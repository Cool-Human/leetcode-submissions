from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjList = {i: [] for i in range(1, n + 1)}
        outgoing = [0] * (n + 1)

        for a, b in trust:
            adjList[b].append(a)
            outgoing[a] += 1

        for judge in range(1, n + 1):
            if len(adjList[judge]) == n - 1 and outgoing[judge] == 0:
                return judge

        return -1