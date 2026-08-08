class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif m + 1 < len(nums) and nums[m] < target and nums[m + 1] > target:
                return m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return l