class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            mapping[a].append(b)
        
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if mapping[node] == []:
                return True
            
            visiting.add(node)
            for prevNode in mapping[node]:
                if not dfs(prevNode):
                    return False
            visiting.remove(node)
            mapping[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True