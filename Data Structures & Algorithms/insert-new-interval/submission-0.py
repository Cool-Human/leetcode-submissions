class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            last_interval = res[-1]
            if interval[0] <= last_interval[1]:
                last_interval[0] = min(last_interval[0], interval[0])
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                res.append(interval)
        
        return res