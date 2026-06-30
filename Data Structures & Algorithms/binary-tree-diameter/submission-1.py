# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        def depth(node):
            nonlocal maxDiameter

            if not node:
                return 0
            
            L = depth(node.left)
            R = depth(node.right)

            maxDiameter = max(maxDiameter, L + R)

            return 1 + max(L, R)
        
        depth(root)

        return maxDiameter
                