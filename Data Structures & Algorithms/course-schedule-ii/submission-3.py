class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        done = {}
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if not preMap[crs]:
                if crs not in done:
                    done[crs] = 0
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            done[crs] = 0
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        if len(done.keys()) < numCourses:
            return []
        return list(done.keys())