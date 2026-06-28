# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        x = deque()
        if root:
            x.append(root)

        level = 0
        while x:
            for i in range(len(x)):
                node = x.popleft()
                if node.left:
                    x.append(node.left)
                if node.right:
                    x.append(node.right)
            level += 1
        return level