class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_vol = 0

        for i in range(len(heights)):
            height = heights[i]
            j = i

            while j < len(heights):
                height = min(height, heights[j])
                max_vol = max(max_vol, height * (j - i + 1))
                j += 1
        
        return max_vol