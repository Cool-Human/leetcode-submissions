class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = []
        for index, num in enumerate(numbers):
            compliment = target - num
            if compliment in seen:
                return [numbers.index(compliment) + 1, index + 1]
            seen.append(num)
        return