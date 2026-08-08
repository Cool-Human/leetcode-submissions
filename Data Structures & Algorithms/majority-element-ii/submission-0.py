from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        freq_nums = Counter(nums)
        res = []

        for num, freq in freq_nums.items():
            if freq > n:
                res.append(num)
        
        return res