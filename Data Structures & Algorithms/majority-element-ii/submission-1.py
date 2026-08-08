class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums) // 3
        res = []

        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j - i > n:
                res.append(nums[i])
            i = j
        
        return res