class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        k = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[k][1]:
                # overlapping
                if intervals[i][1] > intervals[k][1]:
                    intervals[k][1] = intervals[i][1]
            else:
                # new interval
                k += 1
                intervals[k] = intervals[i]
        
        return intervals[:k + 1]