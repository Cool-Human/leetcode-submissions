class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def back(i, total):
            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(sub.copy())
                return
            
            for j in range(i, len(nums)):
                sub.append(nums[j])
                back(j, total + nums[j])
                sub.pop()

        back(0, 0)
        return res