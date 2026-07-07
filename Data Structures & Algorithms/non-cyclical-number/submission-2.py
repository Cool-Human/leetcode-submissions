class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.squareSum(n)
            if n == 1:
                return True
        
        return False
    
    def squareSum(self, n: int) -> int:
        count = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            count += digit
            n = n // 10
        
        return count