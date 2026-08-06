from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        for num, count in nums_count.items():
            if count == 1:
                return num