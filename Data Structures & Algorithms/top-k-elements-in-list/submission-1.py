from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = []
        res = []

        for num, freq in count.items():
            heapq.heappush_max(max_heap, (freq, num))
        
        while k:
            res.append(heapq.heappop_max(max_heap)[1])
            k -= 1
        
        return res