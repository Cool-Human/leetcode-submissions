class Solution:
    def getRow(self, n: int) -> List[int]:
        arr = [1]
        for i in range(1, n + 1):
            arr.append(arr[-1] * (n + 1 - i) // i)
        return arr