import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Helper to calculate squared distance
        def get_dist(point):
            return point[0]**2 + point[1]**2

        def quickSelect(s, e):
            if s >= e:
                return
            
            # OPTIMIZATION: Pick a random pivot to avoid O(n^2) worst case
            pivot_idx = random.randint(s, e)
            points[pivot_idx], points[e] = points[e], points[pivot_idx]
            
            pivot_dist = get_dist(points[e])
            left = s
            
            for i in range(s, e):
                if get_dist(points[i]) <= pivot_dist:
                    points[left], points[i] = points[i], points[left]
                    left += 1
                    
            points[e], points[left] = points[left], points[e]
            
            # Instead of recursing both sides, only recurse the side we need
            if left == k:
                return
            elif left > k:
                quickSelect(s, left - 1)
            else:
                quickSelect(left + 1, e)

        quickSelect(0, len(points) - 1)
        return points[:k]