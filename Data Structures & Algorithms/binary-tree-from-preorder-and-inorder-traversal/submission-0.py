# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None
        
        base = TreeNode(preorder[0])
        base_index = inorder.index(base.val)

        inorder_base_left = inorder[:base_index]
        size_left_subtree = len(inorder_base_left)
        preorder_base_left = preorder[1: 1 + size_left_subtree]

        inorder_base_right = inorder[base_index + 1:]
        preorder_base_right = preorder[1 + size_left_subtree:]

        base.left = self.buildTree(preorder_base_left, inorder_base_left)
        base.right = self.buildTree(preorder_base_right, inorder_base_right)

        return base