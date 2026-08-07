class Solution:
    def numDecodings(self, s: str) -> int:
        a = c = 0
        b = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                a = 0
            else:
                a = b
            
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                a += c
            
            a, b, c = 0, a, b
        
        return b