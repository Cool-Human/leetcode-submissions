class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if nums[i] in check:
                return [check[nums[i]], i]
            else:
                comp = target - nums[i]
                check[comp] = i
        return None