class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if i - nums_dict[nums[i]][-1] <= k:
                    return True
            nums_dict[nums[i]].append(i)
        
        return False