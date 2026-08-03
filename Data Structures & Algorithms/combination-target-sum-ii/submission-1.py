class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        n = len(candidates)

        def dfs(start: int, remaining:int):
            if remaining == 0:
                res.append(path.copy())
                return
            
            prev = -1
            for i in range(start, n):
                num = candidates[i]

                if num == prev:
                    continue
                if num > remaining:
                    break
                
                prev = num
                path.append(num)
                dfs(i + 1, remaining - num)
                path.pop()
        
        dfs(0, target)
        return res