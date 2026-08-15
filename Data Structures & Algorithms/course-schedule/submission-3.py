class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            preMap[a].append(b)
        
        visited = set()
        
        def dfs(event):
            if not preMap[event]:
                return True
            if event in visited:
                return False
            
            visited.add(event)
            for other_events in preMap[event]:
                if not dfs(other_events):
                    return False
            visited.remove(event)
            preMap[event] = []
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True