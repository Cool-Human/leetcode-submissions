class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(h * width, maxArea)
            stack.append(i)
        
        return maxArea