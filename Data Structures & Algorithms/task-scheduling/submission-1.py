from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        intervals = 0
        if not tasks:
            return intervals
        
        freq = Counter(tasks)

        max_freq = 0
        num_of_max = 0
        
        for amt in freq.values():
            if amt > max_freq:
                max_freq = amt
                num_of_max = 1
            elif amt == max_freq:
                num_of_max += 1
        
        intervals = (max_freq - 1) * (n + 1) + num_of_max

        return max(intervals, len(tasks))