from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        characters = Counter(s)
        middle = False
        res = 0

        for i in characters.values():
            if i % 2 == 0:
                res += i
            else:
                res += (i // 2) * 2
                middle = True
        
        return res + 1 if middle else res