class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = []
        even = []
        characters = sorted(list(s))
        
        i = 0
        while i < len(s):
            if i + 1 < len(s) and characters[i] == characters[i + 1]:
                even.append(characters[i])
                i += 2
            else:
                odd.append(characters[i])
                i += 1

        
        return 2 * len(even) + 1 if odd else 2 * len(even)