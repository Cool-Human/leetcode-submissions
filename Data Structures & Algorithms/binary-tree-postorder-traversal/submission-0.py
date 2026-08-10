# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(res, node):
            if not node:
                return
            
            postorder(res, node.left)
            postorder(res, node.right)
            res.append(node.val)
        
        postorder(res, root)
        return res