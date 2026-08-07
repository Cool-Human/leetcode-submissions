class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        resIdx = 0
        resLen = 0
        resEven = False

        # odd length palindrome
        for i in range(len(s)):
            j = 0

            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1
            
            j -= 1
            if 2 * j + 1 > resLen:
                resLen = 2 * j + 1
                resIdx = i
                resEven = False
        
        # even length palindrome
        for i in range(len(s)):
            j = 0

            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                j += 1
            
            if 2 * j > resLen:
                resLen = 2 * j
                resEven = True
                resIdx = i
        
        i = resIdx
        if resEven:
            j = int(resLen / 2) - 1
            return s[i - j: i + j + 2]
        j = int((resLen - 1) / 2)
        return s[i - j: i + j + 1]