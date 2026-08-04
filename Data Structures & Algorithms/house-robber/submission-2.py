class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        memo = [-1] * (n + 1)
        memo[1] = nums[0]
        memo[2] = max(nums[0], nums[1])

        for i in range(3, n + 1):
            memo[i] = max(nums[i - 1] + memo[i - 2], memo[i - 1])
        
        return memo[-1]