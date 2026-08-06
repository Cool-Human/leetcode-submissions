class Solution:
    def reverse(self, x: int) -> int:
        a, b = 2**31 - 1, -2**31
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = -int(str(abs(x))[::-1])
        if res > a or res < b:
            return 0
        else:
            return res