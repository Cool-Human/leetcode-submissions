# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        level = [root]
        res_append = res.append

        while level:
            right_most = level[-1]
            res_append(right_most.val)
            level = [
                child
                for node in level
                for child in (node.left, node.right)
                if child
            ]
        
        return res