class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxRight = [-1 for _ in range(n)]
        for i in range(n - 1):
            maxRight[i] = max(arr[i + 1:])
        return maxRight