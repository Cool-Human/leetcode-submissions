class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == nums[r]:
            if nums[l] == target: return True
            l += 1
        
        low_bound, high_bound = l, r
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[high_bound]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        if target >= nums[pivot] and target <= nums[high_bound]:
            low, high = pivot, high_bound
        else:
            low, high = low_bound, pivot - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False