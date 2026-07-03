class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = count if maxCount < count else maxCount
            else:
                count = 0
        return maxCount