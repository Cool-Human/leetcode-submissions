class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        even = 0
        characters = sorted(list(s))
        
        i = 0
        while i < len(s):
            if i + 1 < len(s) and characters[i] == characters[i + 1]:
                even += 1
                i += 2
            else:
                odd = True
                i += 1

        
        return 2 * even + 1 if odd else 2 * even