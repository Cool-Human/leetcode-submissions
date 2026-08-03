class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()

        def backtracking(idx: int, subAns: list) -> list:
            '''
            idx -> index
            subAns -> combination of kids that are supposed to sum up to target value
            '''

            if sum(subAns) == target:
                res.add(tuple(subAns))
                return
            if sum(subAns) > target:
                return

            if idx == len(candidates):
                return
            
            subAns.append(candidates[idx])
            backtracking(idx + 1, subAns)

            subAns.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtracking(idx + 1, subAns)

            return
        
        backtracking(0, [])
        return [list(item) for item in res]