import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        x = []
        for num in nums:
            heapq.heappush(x, num)
        return [heapq.heappop(x) for _ in range(len(x))]