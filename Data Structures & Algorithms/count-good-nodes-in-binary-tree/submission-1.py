# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(root, val):
            if not root:
                return 0

            if root.val >= val:
                return 1 + isGood(root.left, root.val) + isGood(root.right, root.val)
            
            return isGood(root.left, val) + isGood(root.right, val)
        
        return isGood(root, float('-inf'))