class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                for j in nums_dict[nums[i]]:
                    if abs(j - i) <= k:
                        return True
            nums_dict[nums[i]].append(i)
        
        return False