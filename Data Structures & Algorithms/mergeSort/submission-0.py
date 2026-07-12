# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n <= 1:
            return pairs

        mid = n // 2
        left, right = self.mergeSort(pairs[:mid]), self.mergeSort(pairs[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += left[i:]
        res += right[j:]
        
        return res