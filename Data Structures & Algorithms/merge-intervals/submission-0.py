class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        if len(intervals) == 1:
            return intervals

        for b_start, b_end in intervals[1:]:
            a_start, a_end = res[-1]

            if a_end >= b_start:
                if a_end < b_end:
                    res[-1][1] = b_end
                continue
            
            res.append([b_start, b_end])
        
        return res