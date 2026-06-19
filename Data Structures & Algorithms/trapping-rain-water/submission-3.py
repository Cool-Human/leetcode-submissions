class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        vol_rain = 0
        n = len(height)

        if n == 0:
            return 0

        for i in range(n):

            while stack and height[i] >= height[stack[-1]]:
                h = height[stack.pop()]
                if stack:
                    vol_rain += (min(height[stack[-1]], height[i]) - h) * (i - stack[-1] - 1)
            
            stack.append(i)
        
        return vol_rain