class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums_set1 = set(nums1)
        nums_set2 = set(nums2)
        res1 = []
        res2 = []

        for i in nums_set1:
            if i not in nums_set2:
                res1.append(i)
        for j in nums_set2:
            if j not in nums_set1:
                res2.append(j)
        
        return [res1, res2]