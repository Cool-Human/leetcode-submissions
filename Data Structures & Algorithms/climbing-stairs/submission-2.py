class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            store = [0] * n
            
            store[0] = 1
            store[1] = 2

            for i in range(2, n):
                store[i] = store[i - 1] + store[i - 2]
            
            return store[-1]