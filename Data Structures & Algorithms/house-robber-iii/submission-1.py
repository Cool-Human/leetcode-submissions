# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            
            left_true, left_false = dfs(node.left)
            right_true, right_false = dfs(node.right)

            node_true = node.val + left_false + right_false
            node_false = max(left_true, left_false) + max(right_true, right_false)

            return node_true, node_false
        
        return max(dfs(root))