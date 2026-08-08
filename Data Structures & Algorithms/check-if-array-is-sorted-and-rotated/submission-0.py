class Solution:
    def check(self, nums: List[int]) -> bool:
        broken = False
        i = 0
        while i < len(nums):
            if nums[i] > nums[(i + 1) % len(nums)]:
                if broken:
                    return False
                else:
                    broken = True
            i += 1
        return True