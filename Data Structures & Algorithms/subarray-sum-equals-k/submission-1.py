class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        counts = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in counts:
                res += counts[prefix_sum - k]
            counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
        return res