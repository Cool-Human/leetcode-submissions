# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or (root and not subRoot):
            return True
        
        if not root and subRoot:
            return False
        
        def isSame(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            if root1.val == root2.val:
                return isSame(root1.right, root2.right) and isSame(root1.left, root2.left)
            
            return False
        
        if not isSame(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return True