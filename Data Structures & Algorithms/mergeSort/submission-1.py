# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) < 2:
            return pairs
        
        mid = len(pairs) // 2
        left, right = self.mergeSort(pairs[:mid]), self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        i = j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        
        return res