class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        self.row = len(image)
        self.col = len(image[0])
        self.color = color
        self.initial_color = image[sr][sc]

        def dfs(image, visit, r, c):
            if (min(r, c) < 0) or (r == self.row) or (c == self.col) or (image[r][c] != self.initial_color) or ((r, c) in visit):
                return image
            
            image[r][c] = self.color
            
            visit.add((r, c))

            dfs(image, visit, r + 1, c)
            dfs(image, visit, r - 1, c)
            dfs(image, visit, r, c + 1)
            dfs(image, visit, r, c - 1)

            visit.remove((r, c))

            return image
        
        return dfs(image, visit, sr, sc)