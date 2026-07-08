class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i]
            points[i].insert(0, int((x**2) + (y**2)))
        points.sort(key = lambda x : x[0])
        return [x[1:] for x in points[:k]]