class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_vol = 0

        for i in range(len(heights)):
            height = heights[i]

            r = i + 1
            while r < len(heights) and heights[r] >= height:
                r += 1
            
            l = i
            while l >= 0 and heights[l] >= height:
                l -= 1
            
            r -= 1
            l += 1
            max_vol = max(max_vol, height * (r - l + 1))
        
        return max_vol 