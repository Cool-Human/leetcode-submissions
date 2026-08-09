class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int("".join(str(d) for d in digits)) + 1)]