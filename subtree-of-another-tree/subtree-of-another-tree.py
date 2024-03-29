# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return False
        if root is None and subRoot is not None:
            return False
        
        return self.issame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def issame(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False

        return root.val == subRoot.val and self.issame(root.left, subRoot.left) and self.issame(root.right, subRoot.right)