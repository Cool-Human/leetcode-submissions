class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1)
        return points[:k] if k < len(points) else points
    
    def quickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e][0] ** 2 + arr[e][1] ** 2
        left = s

        for i in range(s, e):
            dis = arr[i][0] ** 2 + arr[i][1] ** 2
            if pivot >= dis:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        arr[e], arr[left] = arr[left], arr[e]

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)