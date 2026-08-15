class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        done = set()
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if not preMap[crs]:
                if crs not in done:
                    res.append(crs)
                    done.add(crs)
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            res.append(crs)
            done.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        if len(res) < numCourses:
            return []
        return res