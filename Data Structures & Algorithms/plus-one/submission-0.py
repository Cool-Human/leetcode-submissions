class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0, 0)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            add = digits[i] + carry
            carry = add // 10
            digits[i] = add % 10
        if digits[0] == 0:
            return digits[1:]
        return digits