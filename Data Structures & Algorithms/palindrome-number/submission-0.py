class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        for a, b in zip(str(x), str(x)[::-1]):
            if a != b:
                return False
        
        return True