class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def back(i, track = [], total = 0):
            if total == target:
                res.append(track[:])
                return
            
            if total > target or i >= len(nums):
                return
            
            track.append(nums[i])
            back(i, track, total + nums[i])

            track.pop()
            back(i + 1, track, total)
        
        back(0)

        return res