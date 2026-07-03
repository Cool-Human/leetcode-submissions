class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = count if maxCount < count else maxCount
                count = 0
        return maxCount if maxCount > count else count